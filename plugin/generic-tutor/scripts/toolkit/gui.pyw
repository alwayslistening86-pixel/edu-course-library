#!/usr/bin/env python3
"""
toolkit/gui.pyw — the toolkit's GUI launcher. Double-click this file (via
pythonw.exe, which a .pyw association runs with no console window) to open
one small control-panel window with a handful of buttons.

DESIGN RULE, non-negotiable: nothing opens except this one control-panel
window until the person clicks something. No window auto-opens a second
window, no window polls or auto-refreshes in the background — a "Refresh"
button re-reads fresh data on demand instead. The point is simple access
without visual noise: Claude's own window stays what you're actually
looking at; this is a status check, not a second front door. Every window
this launcher opens says as much in its own text, so it's never mistaken
for a place to actually study — that happens in a live session via
/continue, not here.

Every button here calls straight into an already-tested, read-only module
(backup.py, health.py, progress.py, review_due.py, errors.py) — this file
is wiring only, no logic of its own beyond formatting.
"""
import json
import os
import sys
import tkinter as tk
from tkinter import scrolledtext, ttk, messagebox

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import core  # noqa: E402
import backup  # noqa: E402
import health  # noqa: E402
import progress  # noqa: E402
import review_due  # noqa: E402
import errors  # noqa: E402

STATUS_LINE = "This is a status view only — study happens in your Claude session via /continue."


def _open_text_window(parent, title, text, on_refresh=None):
    win = tk.Toplevel(parent)
    win.title(title)
    win.geometry("640x480")

    box = scrolledtext.ScrolledText(win, wrap="word", font=("Consolas", 10))
    box.pack(fill="both", expand=True, padx=8, pady=(8, 0))
    box.insert("1.0", text)
    box.configure(state="disabled")

    footer = ttk.Frame(win)
    footer.pack(fill="x", padx=8, pady=8)
    ttk.Label(footer, text=STATUS_LINE, foreground="#666").pack(side="left")

    def _do_refresh():
        new_text = on_refresh()
        box.configure(state="normal")
        box.delete("1.0", "end")
        box.insert("1.0", new_text)
        box.configure(state="disabled")

    if on_refresh:
        ttk.Button(footer, text="Refresh", command=_do_refresh).pack(side="right")
    ttk.Button(footer, text="Close", command=win.destroy).pack(side="right", padx=(0, 8))
    return win


def _fmt(data):
    return json.dumps(data, indent=2, ensure_ascii=False)


class ToolkitApp:
    def __init__(self, root_window):
        self.root_window = root_window
        self.edu_root = core.edu_root()
        self.learners = core.list_learners(self.edu_root)

        root_window.title("generic-tutor toolkit")
        root_window.geometry("320x300")
        root_window.resizable(False, False)

        frame = ttk.Frame(root_window, padding=12)
        frame.pack(fill="both", expand=True)

        ttk.Label(frame, text="Learner:").pack(anchor="w")
        self.learner_var = tk.StringVar(value=self.learners[0] if self.learners else "")
        learner_menu = ttk.Combobox(frame, textvariable=self.learner_var, values=self.learners, state="readonly")
        learner_menu.pack(fill="x", pady=(0, 12))

        if not self.learners:
            ttk.Label(frame, text="No learner profile found yet under\nprofile/ — nothing to show.",
                      foreground="#a33").pack(pady=(0, 12))

        buttons = [
            ("Progress", self.show_progress),
            ("Review due", self.show_review_due),
            ("Errors", self.show_errors),
            ("Health", self.show_health),
            ("Backup now", self.run_backup),
        ]
        for label, command in buttons:
            ttk.Button(frame, text=label, command=command).pack(fill="x", pady=3)

        ttk.Label(frame, text=STATUS_LINE, wraplength=290, foreground="#666",
                  font=("Segoe UI", 8)).pack(pady=(12, 0))

    def _learner(self):
        lid = self.learner_var.get()
        if not lid:
            messagebox.showinfo("No learner selected", "No learner profile found under profile/ yet.")
            return None
        return lid

    def show_progress(self):
        lid = self._learner()
        if not lid:
            return
        _open_text_window(self.root_window, f"Progress — {lid}",
                           _fmt(progress.snapshot(lid, root=self.edu_root)),
                           on_refresh=lambda: _fmt(progress.snapshot(lid, root=self.edu_root)))

    def show_review_due(self):
        lid = self._learner()
        if not lid:
            return
        _open_text_window(self.root_window, f"Review due — {lid}",
                           _fmt(review_due.due_cards(lid, root=self.edu_root, within_slots=5)),
                           on_refresh=lambda: _fmt(review_due.due_cards(lid, root=self.edu_root, within_slots=5)))

    def show_errors(self):
        lid = self._learner()
        if not lid:
            return
        _open_text_window(self.root_window, f"Errors — {lid}",
                           _fmt(errors.aggregate(lid, root=self.edu_root, open_only=True)),
                           on_refresh=lambda: _fmt(errors.aggregate(lid, root=self.edu_root, open_only=True)))

    def show_health(self):
        _open_text_window(self.root_window, "Health",
                           _fmt(health.check_health(root=self.edu_root)),
                           on_refresh=lambda: _fmt(health.check_health(root=self.edu_root)))

    def run_backup(self):
        lid = self._learner()
        if not lid:
            return
        result = backup.create_backup(lid, root=self.edu_root)
        if "error" in result:
            messagebox.showerror("Backup failed", result["error"])
            return
        messagebox.showinfo(
            "Backup complete",
            f"Saved {result['files_written']} files "
            f"({result['size_bytes'] // 1024} KB) to:\n\n{result['zip_path']}",
        )


def main():
    root_window = tk.Tk()
    ToolkitApp(root_window)
    root_window.mainloop()


if __name__ == "__main__":
    main()
