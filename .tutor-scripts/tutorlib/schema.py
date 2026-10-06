"""
Minimal JSON Schema validator (S-06) -- stdlib only, no third-party dependency.

Supports the subset the tutor's schemas use: type (incl. unions; "integer" excludes
bool), enum, const, required, properties, patternProperties, additionalProperties
(bool or schema), items, minItems, minimum, maximum, minLength, pattern, oneOf, anyOf,
allOf, and local "$ref": "#/definitions/<name>". Unknown keywords are ignored (so the
schema files remain valid JSON Schema draft 2020-12 documents for other tools).

Schemas live in tutorlib/schemas/<kind>.json and are deployed with the package.
"""
import json
import os
import re

SCHEMA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "schemas")

_TYPES = {
    "object": lambda v: isinstance(v, dict),
    "array": lambda v: isinstance(v, list),
    "string": lambda v: isinstance(v, str),
    "number": lambda v: isinstance(v, (int, float)) and not isinstance(v, bool),
    "integer": lambda v: isinstance(v, int) and not isinstance(v, bool),
    "boolean": lambda v: isinstance(v, bool),
    "null": lambda v: v is None,
}


def kinds():
    return sorted(f[:-5] for f in os.listdir(SCHEMA_DIR) if f.endswith(".json"))


def load(kind):
    with open(os.path.join(SCHEMA_DIR, f"{kind}.json"), encoding="utf-8") as f:
        return json.load(f)


def validate_output(instance, name):
    """Errors for a script's JSON *output* against `schemas/outputs/<name>.json` (the shapes skills are allowed to quote)."""
    with open(os.path.join(SCHEMA_DIR, "outputs", f"{name}.json"), encoding="utf-8") as f:
        sch = json.load(f)
    errors = []
    _check(instance, sch, sch, "", errors)
    return errors


def _resolve(ref, root):
    node = root
    for part in ref.lstrip("#/").split("/"):
        node = node[part]
    return node


def _check(value, schema, root, path, errors):
    if "$ref" in schema:
        _check(value, _resolve(schema["$ref"], root), root, path, errors)
        return
    for sub in schema.get("allOf", []):
        _check(value, sub, root, path, errors)
    t = schema.get("type")
    if t is not None:
        names = t if isinstance(t, list) else [t]
        if not any(_TYPES[n](value) for n in names):
            errors.append(f"{path or '$'}: expected {'|'.join(names)}, got {type(value).__name__}")
            return
    if "const" in schema and value != schema["const"]:
        errors.append(f"{path or '$'}: must equal {schema['const']!r}")
    if "enum" in schema and value not in schema["enum"]:
        errors.append(f"{path or '$'}: {value!r} not in {schema['enum']}")
    for key, test, msg in (("minimum", lambda v, m: v >= m, "below minimum"), ("maximum", lambda v, m: v <= m, "above maximum")):
        if key in schema and _TYPES["number"](value) and not test(value, schema[key]):
            errors.append(f"{path or '$'}: {value!r} {msg} {schema[key]}")
    if isinstance(value, str):
        if "minLength" in schema and len(value) < schema["minLength"]:
            errors.append(f"{path or '$'}: shorter than {schema['minLength']}")
        if "pattern" in schema and not re.search(schema["pattern"], value):
            errors.append(f"{path or '$'}: {value!r} does not match {schema['pattern']}")
    if isinstance(value, list):
        if "minItems" in schema and len(value) < schema["minItems"]:
            errors.append(f"{path or '$'}: fewer than {schema['minItems']} items")
        if "items" in schema:
            for i, item in enumerate(value):
                _check(item, schema["items"], root, f"{path}[{i}]", errors)
    if isinstance(value, dict):
        for r in schema.get("required", []):
            if r not in value:
                errors.append(f"{path or '$'}: missing required '{r}'")
        props = schema.get("properties", {})
        patterns = schema.get("patternProperties", {})
        addl = schema.get("additionalProperties", True)
        for k, v in value.items():
            sub_path = f"{path}.{k}" if path else k
            matched = False
            if k in props:
                matched = True
                _check(v, props[k], root, sub_path, errors)
            for pat, sub in patterns.items():
                if re.search(pat, k):
                    matched = True
                    _check(v, sub, root, sub_path, errors)
            if not matched:
                if addl is False:
                    errors.append(f"{sub_path}: unexpected property")
                elif isinstance(addl, dict):
                    _check(v, addl, root, sub_path, errors)
    if "anyOf" in schema and not any(not _sub_errors(value, s, root, path) for s in schema["anyOf"]):
        errors.append(f"{path or '$'}: matches none of the allowed shapes")
    if "oneOf" in schema:
        n = sum(1 for s in schema["oneOf"] if not _sub_errors(value, s, root, path))
        if n != 1:
            errors.append(f"{path or '$'}: must match exactly one allowed shape (matched {n})")


def _sub_errors(value, schema, root, path):
    errs = []
    _check(value, schema, root, path, errs)
    return errs


def validate(instance, kind):
    """Return a list of human-readable error strings (empty = valid)."""
    schema = load(kind)
    errors = []
    _check(instance, schema, schema, "", errors)
    return errors


def validate_file(path, kind):
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
    except (OSError, ValueError) as e:
        return [f"unreadable: {type(e).__name__}: {e}"]
    return validate(data, kind)
