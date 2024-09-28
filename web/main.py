import pyautogui
import time

# Open Notepad application
pyautogui.press('winleft')
pyautogui.typewrite('notepad++')
pyautogui.press('enter')
time.sleep(1)

# Type a message
pyautogui.typewrite("Hello, world!")

# Save the file
pyautogui.hotkey('ctrl', 's')
time.sleep(1)
pyautogui.typewrite("example.txt")
pyautogui.press('enter')
