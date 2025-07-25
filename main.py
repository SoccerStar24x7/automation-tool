import keyboard as builtin_kbd # to see if a key is pressed at a spontaneous time

import pynput.keyboard as keyboards

import pynput.mouse as mouse

import time
import json

# Remove last ctrl by using for loop starting from end of scripts.json, and removing the first value that's ctrl

keyboard = keyboards.Controller()
smouse = mouse.Controller()

def identify_modifier(key):
    print(f"we should print {key} with type {type(key)}")
    if key == "Key.enter":
        print("enter")
        keyboard.press(keyboards.Key.enter)

        keyboard.release(keyboards.Key.enter)

    elif key == "Key.space":
        print("space")
        keyboard.press(keyboards.Key.space)
        keyboard.release(keyboards.Key.space)

    elif key in ["Key.shift", "Key.shift_r", "Key.shift_l"]:
        print("shift")
        keyboard.press(keyboards.Key.shift)
        keyboard.release(keyboards.Key.shift)

    elif key == "Key.tab":
        print("tab")
        keyboard.press(keyboards.Key.tab)
        keyboard.release(keyboards.Key.tab)

    elif key in ["Key.ctrl_l", "Key.ctrl_r", "Key.ctrl"]:
        print("ctrl")
        keyboard.press(keyboards.Key.ctrl)
        keyboard.release(keyboards.Key.ctrl)

    elif key == "Key.caps_lock":
        print("caps lock")
        keyboard.press(keyboards.Key.caps_lock)
        keyboard.release(keyboards.Key.caps_lock)

    elif key == "Key.backspace":
        print("caps lock")
        keyboard.press(keyboards.Key.backspace)
        keyboard.release(keyboards.Key.backspace)

    elif key in ["Key.alt", "Key.alt_r"]:
        print("alt")
        keyboard.press(keyboards.Key.alt)
        keyboard.release(keyboards.Key.alt)

    else:
        print("REALY PRINT")

        # chatgpt magic
        keycode = keyboards.KeyCode.from_char(key.strip("'"))  # strip quotes if needed
        keyboard.press(keycode)
        keyboard.release(keycode)
        



def watch():
    print("Hotkey to end program is \"Ctrl+4\"\n") # gives warning to user about hotkey
 

    events = {} # creates dictionary for events 

    orgTime = time.time() # original time when program was started

    def on_mouse_click(x, y, button, pressed):

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
    keyboard_listener = keyboards.Listener(on_press=on_kbd_press)
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

        curMouseX, curMouseY = smouse.position # gets the mouse position


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
        if builtin_kbd.is_pressed('ctrl+4'):
            print("higher authority doesn't like us 😔")
            exit()

        curTime = round((time.time() - orgTime), 2)

        print(f"{float(eventTime)}-{curTime} = {float(eventTime)-curTime}")

        try:
            time.sleep(float(eventTime)-curTime)

        except ValueError:
            print("uh oh")
            

        print(f"{eventTime}: {logs[eventTime]}")

        print(curTime)


        # print((float(eventTime) - curTime))
        # time.sleep((float(eventTime) - curTime)) # waits until the time is right

        event = logs[eventTime]

        if type(event) == list: # if the event recorded the mouse position
            mouseX, mouseY = event

            smouse.position = mouseX, mouseY

        elif "click" in event:

            if event == "Lclick": # if the event recorded a left click
                smouse.click(mouse.Button.left, 1)
        
            elif event == "Rclick": # if the event recorded a right click
                smouse.click(mouse.Button.right, 1)

            elif event == "Mclick": # if the event recorded a right click
                smouse.click(mouse.Button.middle, 1)
        
        else:
            print("PRINT TIME")
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
