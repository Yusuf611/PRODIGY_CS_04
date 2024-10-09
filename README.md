## 📜 Project Overview
This **Simple Keylogger** is a Python-based project that records and logs keystrokes made on a keyboard and saves them to a text file. This tool demonstrates how keylogging works in practice and is designed **strictly for educational purposes** to promote understanding of cybersecurity risks and how keyloggers can be detected.

## ⚠️ Disclaimer
This project is intended **only for educational purposes**. Misusing this project to log keystrokes without permission is illegal and unethical. Always ensure you have the proper consent to monitor any system.

## 🚀 Features
- Logs all keypresses (including special keys like `Enter` and `Space`).
- Saves the logged keystrokes in a `.txt` file.
- Simple to use with customizable start and stop functions.

## 🛠️ Installation

### Prerequisites
- Python 3.x
- `pynput` library

### Steps:
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/simple-keylogger.git
   cd simple-keylogger

Install the required library:
``bash
pip install pynput

``bash
python keylogger.py

✨ Usage
The keylogger will start logging keystrokes once the program is running.
All recorded keystrokes will be saved in keylog.txt.
Press the Esc key to stop logging.
Example:
After running the script, type normally, and your keystrokes will be recorded in the file keylog.txt.
To stop the keylogger, press Esc.
📚 How it Works
This program uses the pynput library to monitor keyboard inputs in real-time. Every keystroke is captured and saved to a file. The logger is designed to run silently, with the option to stop logging by pressing Esc.

🎯 Educational Purpose
The project demonstrates:

How keyloggers can work.
The importance of cybersecurity awareness.
How to detect and prevent malicious keyloggers in a real-world scenario.
