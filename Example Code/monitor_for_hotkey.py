'''This is a example code snippit of how to listen for a hotkey '''

from pynput import keyboard

# The key combination to check
COMBINATIONS = [
    {keyboard.Key.shift, keyboard.KeyCode(char='a')},
    {keyboard.Key.shift, keyboard.KeyCode(char='A')}
]

# The currently active modifiers
current = set()

def execute():
    print ("Do Something")

def on_press(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
            execute()

def on_release(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        ## Adding Try, except as heavy spam can cause crash
        try:
            current.remove(key)
        except:
            pass

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
