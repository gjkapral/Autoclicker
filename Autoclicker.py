#Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
#Type "help", "copyright", "credits" or "license()" for more information.
import time
import pynput
import random

from pynput.keyboard import Key, Controller
keyboard = Controller()

for x in range (0,500):
    z = random.randint(1,10)
    time.sleep(z)
    keyboard.press('1')
    keyboard.release('1')
    x+=1
 
