from pynput.keyboard import Key, Controller

keyboard = Controller()

keyboard.release(Key.alt)
keyboard.release(Key.shift)
keyboard.release(Key.ctrl)
keyboard.release(Key.caps_lock)