import pyautogui as gui
import keyboard as kbd
import time
import json

screenWidth, screenHeight = gui.size() # Get the size of the primary monitor.

def watch():
    print("Hotkey to end program is \"Ctrl+l\"")

    mouseXs = []
    mouseYs = []
    times = []
    LclickTimes = []
    RclickTimes = []

    events = {}


    orgTime = time.time()

    while not(kbd.is_pressed('ctrl+l')):
        
        curTime = round((time.time() - orgTime), 2)

        curMouseX, curMouseY = gui.position()

        events[f"{curTime}"] = [curMouseX, curMouseY]

        print(events)
        """
        mouseXs.append(curMouseX)
        mouseYs.append(curMouseY)
        times.append('%.3f'%(time.time() - orgTime))

        """

        time.sleep(1) # change to 0.1 in final build
    


    data = json.dumps(events)
    with open("scripts.json", "w") as f:
            f.write(data)
    


    print(data)

    



def do():
    pass



watch()