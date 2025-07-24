import pyautogui as gui
import keyboard as builtin_kbd
from pynput import mouse
from pynput import keyboard as pynput_kbd
from pynput.keyboard import Key, Controller
import time
import json

# keyboard shit is fucked



screenWidth, screenHeight = gui.size() # Get the size of the primary monitor.

keyboard = Controller()

def identify_modifier(key):
    if key == "Key.enter":
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

    elif key == "Key.space":
        keyboard.press(Key.space)
        keyboard.release(Key.space)

    elif key == "Key.shift" or "Key.shift_r" or "Key.shift_l":
        keyboard.press(Key.shift)
        keyboard.release(Key.shift)

    elif key == "Key.tab":
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)

    elif key == "Key.ctrl_l" or "Key.ctrl_r" or "Key.ctrl":
        keyboard.press(Key.ctrl)
        keyboard.release(Key.ctrl)

    elif key == "Key.caps_lock":
        keyboard.press(Key.caps_lock)
        keyboard.release(Key.caps_lock)

    elif key == "Key.alt" or "Key.alt_r":
        keyboard.press(Key.alt)
        keyboard.release(Key.alt)

    else:
        keyboard.type(key)
        



def watch():
    print("Hotkey to end program is \"Ctrl+4\"\n") # gives warning to user about hotkey
 

    events = {} # creates dictionary for events 

    orgTime = time.time() # original time when program was started

    def on_mouse_click(x, y, button, pressed):
        orgTime = time.time() # original time when program was started

        if button == mouse.Button.left: # if left button was clicked

            curTime = round((time.time() - orgTime), 2) # gets the time

            events[f"{curTime}"] = "Lclick" 
            

        elif button == mouse.Button.right: # if right button was clicked
            
            curTime = round((time.time() - orgTime), 2) # gets the time

            events[f"{curTime}"] = "Rclick"

        else: # if middle button was clicked
            curTime = round((time.time() - orgTime), 2) # gets the time

            events[f"{curTime}"] = "Mclick"


    def on_kbd_press(key):

        curTime = round((time.time() - orgTime), 2) # gets the time
        print(f"{key} key pressed at {curTime}.")

        events[f"{curTime}"] = f"{key}"



    mouse_listener = mouse.Listener(on_click=on_mouse_click)
    keyboard_listener = pynput_kbd.Listener(on_press=on_kbd_press)
    mouse_listener.start()
    keyboard_listener.start()

    tempTime = 0

    while not(builtin_kbd.is_pressed('ctrl+4')): # if Ctrl+L is not pressed (Ctrl+L is hotkey to end recording)

        
        if tempTime != 4:
            tempTime += 1
            continue

        else:
            tempTime = 0
                
        curTime = round((time.time() - orgTime), 2) # gets the time during that loop, and subtracts it by original
                                                    # time to get time since recording started

        curMouseX, curMouseY = gui.position() # gets the mouse position


        if f"{curTime}" not in events:
            events[f"{curTime}"] = [curMouseX, curMouseY] # adds to the events dict., the time as 
                                                          # the key and the mouse position as the value

        # time.sleep(0.01) # delays time to avoid burnout 
        tempTime += 1
    

    mouse_listener.stop()
    keyboard_listener.stop()

    data = json.dumps(events) # converts events to json-ready format
    with open("scripts.json", "w") as w: # opens the json
        w.write(data) # writes our data to the json

    



def do():
    with open("scripts.json", "r") as f:
        logs = json.load(f)

    orgTime = time.time()

    for eventTime in logs: 
        print(f"{eventTime}: {logs[eventTime]}")

        curTime = round((time.time() - orgTime), 2)
        print(curTime)


        # print((float(eventTime) - curTime))
        # time.sleep((float(eventTime) - curTime)) # waits until the time is right

        event = logs[eventTime]

        if type(logs[eventTime]) == list: # if the event recorded the mouse position
            mouseX, mouseY = event

            gui.moveTo(mouseX, mouseY)

        elif "click" in event:
            if event == "Lclick": # if the event recorded a left click
                gui.click(button="left")
        
            elif event == "Rclick": # if the event recorded a right click
                gui.click(button="right")

            elif event == "Mclick": # if the event recorded a right click
                gui.click(button="middle")
        
        else:
            identify_modifier(event)           
            
                
                
def main():
    func = input("What operation do you want (watch or do)?: ")
    print()

    if func == "watch":
        watch()

    elif func == "do":
        do()

    else:
        print("dumbahh")

main()
