# Dependencies: keyboard, mouse. Install them via "pip install keyboard". "pip install mouse"
# You also need to install Autohotkey
# APM Manager

import keyboard
import mouse
import time
from subprocess import Popen
import os
import configparser

global actionCounter

# Read
config = configparser.ConfigParser()
config.sections()
config.read('settings.ini')

startkey = '/' # Numpad /
stopkey = 55 # Numpad *


maxActions = int(config['settings']['actions'])
seconds = int(config['settings']['seconds'])

APM=maxActions/seconds
print('Your APM will be ~ ' + str(int(APM*60)))

allowedKeys = [15, 29, 42, 56, 58, 91, 59, 60, 61, 62, 63, 64, 65,
               66]  # codes for alt,windows,ctrl,shift,capslock,tab,         f1,f2,f3,f4,f5,f6,f7,f8


def keyPressed(e):
    global actionCounter
    global maxActions
    if e.scan_code == 74:
        os._exit(0)
    if e.scan_code in allowedKeys:
        pass
    else:
        print(e.name + ' ' + e.event_type + ' Scan-Code: ' + str(e.scan_code))
        actionCounter = actionCounter + 1 / 2
        if actionCounter >= maxActions:
            blockKeyboard()
            print("Blocked: " + e.name + ' ' + e.event_type + ' Scan-Code: ' + str(e.scan_code))


def blockKeyboard():
    for i in range(150):
        if i in allowedKeys:
            pass
        else:
            keyboard.block_key(i)


def mouseleft():
    global actionCounter
    global maxActions
    print('left click')
    actionCounter = actionCounter + 1
    if actionCounter >= maxActions:
        keyboard.send(startkey)
        print("Blocked: MouseLeft")


def mouseright():
    global actionCounter
    global maxActions
    print('right click')
    actionCounter = actionCounter + 1
    if actionCounter >= maxActions:
        keyboard.send(startkey)
        print("Blocked: MouseLeft")


mouse.on_click(mouseleft)
mouse.on_right_click(mouseright)

while True:
    actionCounter = 0  # reset key-counter
    keyboard.unhook_all()  # reset keyboard-blocking
    keyboard.send(stopkey)
    keyboard.hook(keyPressed)  # block keyboard function
    time.sleep(seconds)
