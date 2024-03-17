import pyautogui
from time import sleep
sleep(4)
for i in range(0, 10):
    pyautogui.write('Hello Python, what\'s up', interval=0.25)
    pyautogui.press('enter')

