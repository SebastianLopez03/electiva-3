import pyautogui
import time

time.sleep (5)
text = 'Network automation exercise using Python'

pyautogui.typewrite(text)

time.sleep(2)
pyautogui.press('enter')
