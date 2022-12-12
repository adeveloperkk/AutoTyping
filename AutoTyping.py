import pyautogui
import time 
time.sleep(3)
for i in range(100):
    pyautogui.typewrite("Enter Your Text Here")
    pyautogui.press("enter")