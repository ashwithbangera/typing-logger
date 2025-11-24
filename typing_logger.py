#!/usr/bin/env python3

import tkinter as tk
from datetime import datetime
import os

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "keystrokes.txt")

os.makedirs(LOG_DIR, exist_ok=True)

def append_log(entry: str):
    timestamp = datetime.utcnow().isoformat() + "Z"
    line = f"{timestamp}\t{entry}\n"
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line)

class TypingLoggerApp:
    def __init__(self, root):
        self.root = root
        root.title("Typing Logger (Safe Demo)")
        root.geometry("600x350")

        self.label = tk.Label(root, text="Type inside the box. Keys are logged safely.")
        self.label.pack(pady=10)

        self.text = tk.Text(root, height=12, wrap="word")
        self.text.pack(fill="both", padx=10, pady=10)
        self.text.focus_set()

        self.text.bind("<Key>", self.on_key)

    def on_key(self, event: tk.Event):
        char = event.char
        keysym = event.keysym

        if char and char.isprintable():
            entry = f"CHAR: {char!r}"
        else:
            entry = f"KEY: {keysym}"

        append_log(entry)
        return None

def main():
    root = tk.Tk()
    app = TypingLoggerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
