import pyautogui as gui
import keyboard as kbd
import time
import json


screenWidth, screenHeight = gui.size() # Get the size of the primary monitor.

def watch():
    print("Hotkey to end program is \"Ctrl+l\"") # gives warning to user about hotkey
    print("Hotkey to record click is: \n\"Ctrl+Alt+G\" for left clicks, \nAnd \"Ctrl+Alt+H\" for right clicks.")
    print("I recommend that when you use any of the hotkeys, you do\n the hotkey mulitple timesfor the hotkey to actually register.\n")

    mouseXs = []
    mouseYs = []
    times = []
    LclickTimes = []
    RclickTimes = []

    events = {} # creates dictionary for events 

    orgTime = time.time() # original time when program was started

    while not(kbd.is_pressed('ctrl+l')): # if Ctrl+L is not pressed (Ctrl+L is hotkey to end recording)
        
        curTime = round((time.time() - orgTime), 2) # gets the time during that loop, and subtracts it by original
                                                    # time to get time since recording started

        curMouseX, curMouseY = gui.position() # gets the mouse position

        # events[f"{curTime}"] = [curMouseX, curMouseY] # adds to the events dict., the time as 
                                                      # the key and the mouse position as the value

        if kbd.is_pressed('ctrl+alt+g'):
            print(f"Left click detected at {curTime}.")
            events[f"{curTime}"] = "Lclick"

        if kbd.is_pressed('ctrl+alt+h'):
            print(f"Right click detected at {curTime}.")
            events[f"{curTime}"] = "Rclick"


        print(events) # DEBUG
        """
        mouseXs.append(curMouseX)
        mouseYs.append(curMouseY)
        times.append('%.3f'%(time.time() - orgTime))

        """

        time.sleep(0.5) # change to 0.1 in final build
    


    data = json.dumps(events) # converts events to json-ready format
    with open("scripts.json", "w") as w: # opens the json
        w.write(data) # writes our data to the json

    



def do():
    with open("scripts.json", "r") as f:
        logs = json.load(f)

    orgTime = time.time()

    for key in logs:

        curTime = round((time.time() - orgTime), 2)

        if curTime != key:
            time.sleep(key-curTime)
    
        

    



watch()


def main():
    pass