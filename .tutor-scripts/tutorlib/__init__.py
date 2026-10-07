"""
tutorlib -- shared plumbing for the tutor's scripts (E-02).

Deliberately small and stdlib-only. Deployed to .tutor-scripts/tutorlib/ by
bootstrap_scripts.py (any subfolder with an __init__.py ships as a package), so
scripts can simply `from tutorlib import atomic_io`.

  atomic_io  crash-safe JSON writes (temp file + fsync + os.replace)
  filelock   advisory per-file lock for read-modify-write sequences
"""
