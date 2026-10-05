#!/usr/bin/env python3
"""
record_mock.py -- record the result of a mock paper (L-08).

    python3 record_mock.py <subjects.json> <total_marks> <marks_awarded> <minutes_taken> <today YYYY-MM-DD> [question_ids_csv]

Appends `{date, total_marks, awarded, percent, minutes, questions}` to the learner's `mock_results` (most recent last, at most 20
kept). A mock is practice under approximate conditions: it never changes `syllabus_status`, never unlocks or locks anything and is
not a grade - `readiness.py` reports the latest mocks beside, not inside, its band. Consent class: signal (a performance record), so
it is kept under `granted` only. Written atomically under the file lock and ledgered.
"""
import datetime
import json
import sys

from tutorlib import atomic_io, cli, consent, filelock, ledger, state

KEEP = 20


@ledger.logged("record_mock.py", "subjects_path")
@filelock.locked("subjects_path")
def record(subjects_path, total_marks, awarded, minutes, today_iso, question_ids=None):
    try:
        datetime.date.fromisoformat(today_iso)
    except ValueError:
        return {"error": "today must be YYYY-MM-DD"}
    if not (isinstance(total_marks, int) and total_marks > 0 and isinstance(awarded, int) and 0 <= awarded <= total_marks):
        return {"error": f"need 0 <= marks_awarded ({awarded}) <= total_marks ({total_marks}) and total_marks > 0"}
    if not (isinstance(minutes, int) and minutes >= 0):
        return {"error": "minutes_taken must be a non-negative integer"}
    data = state.load(subjects_path, "subjects")
    entry = {"date": today_iso, "total_marks": total_marks, "awarded": awarded, "percent": round(100 * awarded / total_marks, 1),
             "minutes": minutes, "questions": list(question_ids or [])}
    history = [m for m in data.get("mock_results", []) if isinstance(m, dict)] + [entry]
    data["mock_results"] = history[-KEEP:]
    allowed, status = consent.check(subjects_path, consent.SIGNAL)
    if not allowed:
        return {"action": "record", "mock": entry, **consent.skipped(status, consent.SIGNAL)}
    atomic_io.write_json(subjects_path, data)
    return {"action": "record", "mock": entry, "written": True, "mocks_on_file": len(data["mock_results"])}


def main(argv):
    if len(argv) not in (5, 6):
        print(json.dumps({"error": "usage: record_mock.py <subjects.json> <total_marks> <marks_awarded> <minutes_taken> <today> [question_ids_csv]"}))
        return 2
    try:
        ids = [q for q in (argv[5].split(",") if len(argv) == 6 else []) if q]
        return cli.emit(record(argv[0], int(argv[1]), int(argv[2]), int(argv[3]), argv[4], ids))
    except ValueError:
        print(json.dumps({"error": "total_marks, marks_awarded and minutes_taken must be integers"}))
        return 2
    except cli.EXPECTED_ERRORS as e:
        print(json.dumps({"error": f"{type(e).__name__}: {e}"}))
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
