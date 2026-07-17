import subprocess
import json
import time
import os

with open("rwi.json", "r") as f:
    settings = json.load(f)

if settings["notify_on_start"]: subprocess.run(
    ["notify-send", "RWI started"]
)

def window_check_and_kill(window_name, word_list):
    if (any(word.lower() in window_name.lower() for word in word_list)):
        os.kill(int(result[14].split("pid:", 1)[1]), 9)
    

while True:
    result = subprocess.run(
        ["hyprctl", "activewindow"],
        capture_output=True,
        text=True
    ).stdout.splitlines()

    current_window = result[11].split("title:", 1)[1]

    window_check_and_kill(current_window, settings["blocked"])

    if (settings["is_work_mode_active"]):
        window_check_and_kill(current_window, settings["work_block"])
    
    time.sleep(0.5)