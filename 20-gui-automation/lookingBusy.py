#! python3
# lookingBusy.py - Nudge mouse cursor every 10 seconds to avoid being idle.

import pyautogui, random

try:
    while True:
        choices = (-5, 5)
        pyautogui.move(random.choice(choices), random.choice(choices), duration=0.1)
        pyautogui.sleep(10)
except KeyboardInterrupt:
    print('Done!')
