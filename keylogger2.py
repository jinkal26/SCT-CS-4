
# Purpose: educational/demo only — logs keys typed into this app window.
# IMPORTANT: use only with explicit user consent.

import tkinter as tk
from datetime import datetime

LOGFILE = "keystrokes.log"

def log_key(event):
    """Called on every keypress inside the app window."""
    # event.char is the printable character ('' for special keys)
    # event.keysym is a human-friendly key name (Return, BackSpace, etc.)
    timestamp = datetime.utcnow().isoformat() + "Z"
    char = event.char if event.char else "<no-char>"
    entry = f"{timestamp}\tkeysym={event.keysym}\tchar={repr(char)}\n"
    # Append to log file
    with open(LOGFILE, "a", encoding="utf-8") as f:
        f.write(entry)

def main():
    root = tk.Tk()
    root.title("Safe In-App Key Logger (Demo)")

    label = tk.Label(root, text="Type in the text area below. This app logs keys to keystrokes.log")
    label.pack(padx=10, pady=(10, 0))

    text = tk.Text(root, width=60, height=15)
    text.pack(padx=10, pady=10)
    text.focus_set()

    # Bind key events for the Text widget only
    text.bind("<Key>", log_key)

    # Provide an explicit stop/quit button so user can close
    btn_frame = tk.Frame(root)
    btn_frame.pack(pady=(0,10))
    tk.Button(btn_frame, text="Save & Quit", command=root.destroy).pack(side="left", padx=5)
    tk.Button(btn_frame, text="Show Log", command=lambda: show_log()).pack(side="left", padx=5)

    root.mainloop()

def show_log():
    """Open the log file and print its contents to stdout (for demo)."""
    try:
        with open(LOGFILE, "r", encoding="utf-8") as f:
            print("=== Log contents ===")
            print(f.read())
            print("====================")
    except FileNotFoundError:
        print("Log file not found.")

if __name__ == "__main__":
    main()
