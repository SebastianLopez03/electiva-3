import pyautogui
import time

pyautogui.hotkey('win','r')

time.sleep(2)

pyautogui.write('msedge.exe "facebook.com"', interval=1)
time.sleep(2)

pyautogui.press('Enter')
