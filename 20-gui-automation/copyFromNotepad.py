#! python3
# copyFromNotepad.py - Copies text via clipboard from Notepad.

import pyautogui, pyperclip

wnds = pyautogui.getWindowsWithTitle('Notepad')
if len(wnds) > 0:
    top, left = wnds[0].topleft
    pyautogui.click(top + 300, left + 100)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.sleep(0.1)
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.sleep(0.1)
    text = pyperclip.paste()
    print(text)
