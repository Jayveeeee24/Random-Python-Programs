import pyautogui as gui
import time
import random, string

stri = "hoy walang ganon. kaya ka nga kinakausalp eh para marealizse moubng mga bagay"


number = input("Enter a number: ")
for i in range(int(number)):
    gui.typewrite(stri)
    gui.press('Enter')
    time.sleep(1)
