
# Typing Logger (Safe & Ethical Key Logging Demo)

This project is a **safe keystroke logging application** created for internship learning purposes.  
It logs only the keys typed inside the application window and does NOT run in the background.

---

## 🚀 Features

- Logs every key pressed **only inside the app window**
- Shows a text area where the user types
- Saves keystrokes to a timestamped log file
- Simple Tkinter GUI
- Ethical and safe for educational use

---

## 📂 Project Structure

```

typing-logger/
├── typing_logger.py
├── README.md
└── logs/
└── keystrokes.txt (created automatically)

````

---

## 🔧 How to Run

```bash
python3 typing_logger.py
````

A GUI window will open.
Start typing inside the text box — the keystrokes will be logged.

---

## 📁 Log File

Logs are saved to:

```
logs/keystrokes.txt
```

Each entry looks like:

```
2025-11-24T14:12:30Z    CHAR: 'a'
2025-11-24T14:12:31Z    KEY: BackSpace
```

---

## 📌 Use Cases

* Typing analysis
* Accessibility testing
* GUI input handling demonstration
* Internship/learning project about events and logging

---

## ⚠️ Ethical Notice

This is **not a hidden or background keylogger**.
It only records keys typed inside the visible application window, with user knowledge.

---


