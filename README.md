# Educational Keylogger Using `pynput`

⚠️ **DISCLAIMER**

This project is created strictly for **educational purposes**—to demonstrate how keyboard event capturing works using Python’s `pynput` library.

**Do not use this code on anyone else's system without their clear and informed consent.** Misusing this code can be illegal and unethical. You are solely responsible for how you use it.

---

##  Overview

This script logs keyboard input and stores the key presses along with timestamps in a `.csv` file.

### Features:
- Logs keys with time elapsed between presses.
- Saves to a readable CSV file.
- Stops cleanly on `Ctrl + Q`.

---

##  Usage

### Prerequisites

Install pynput:
   bash
pip install pynput

##  Run the script
python keylogger.py

### Stop the logger
Press Ctrl + Q to stop the program.

### Output
A keylog.csv file is saved under C:\keylogger_test with the following columns:
Timestamp
Key
Elapsed Time (in seconds)

### Legal and Ethical Use
This script is for testing, learning, and self-research on systems you own or have explicit permission to monitor. Unauthorized use may be a violation of:

Privacy laws

Employment agreements

Terms of service


