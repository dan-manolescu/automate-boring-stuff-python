#! python3
# spiralDraw.py _ Use the 5s pause at the beginning to go to Paint and select a brush.

import pyautogui

pyautogui.sleep(5)
pyautogui.click()  # Click to make the window active.
distance = 300
change = 20
while distance > 0:
    pyautogui.drag(distance, 0, duration=0.2)  # Move right.
    distance -= change
    pyautogui.drag(0, distance, duration=0.2)  # Move down.
    pyautogui.drag(-distance, 0, duration=0.2)  # Move left.
    distance -= change
    pyautogui.drag(0, -distance, duration=0.2)  # Move up.
