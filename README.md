# 📝 Typing Logger (Basic Keylogger)

A simple Python-based keylogger that records every key pressed on the keyboard and saves the logs into a text file.
This project is created for learning and educational purposes only — do not use it for any unauthorized activity.

---

## ⚠️ Disclaimer

This keylogger is strictly for ethical use, such as:

* Learning how event listeners work
* Understanding keyboard hooks
* Cybersecurity research in a controlled environment

Do NOT use this tool on anyone's system without permission.
Misuse can lead to legal consequences.

---

## 📌 Features

* Logs every key pressed
* Automatically stores keystrokes in a text file
* Runs in the background
* Lightweight & beginner-friendly
* Uses the `pynput` library for keyboard monitoring

---

## 🛠️ Installation

1. Clone the repository

```bash
git clone https://github.com/ashwithbangera/typing-logger.git
cd typing-logger
```

2. Install dependencies

Make sure Python3 and pip are installed.

```bash
pip install pynput
```

---

## ▶️ How to Run the Keylogger

Run the script using:

```bash
python3 keylogger.py
```

Logs will be saved to:

```
key_log.txt
```

---

## 📂 Project Structure

```
typing-logger/
│── keylogger.py       # Main keylogger script
│── key_log.txt        # Log file (auto-created)
│── README.md          # Project documentation
```

---

## 💡 How It Works

* Uses pynput.keyboard.Listener to capture keystrokes
* Every key pressed is written into `key_log.txt`
* Special keys (Enter, Space, Shift, etc.) are converted into readable text

Example output:

```
h e l l o   w o r l d [ENTER]
```

---
✔ Project banner image

