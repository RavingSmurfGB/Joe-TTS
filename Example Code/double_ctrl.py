'''This listents for ctrl +c pressed in under a second'''
from pynput import keyboard
import datetime

# The key combinations to check
COMBINATIONS = [
    {keyboard.Key.ctrl_l, keyboard.KeyCode(char='c')},
    {keyboard.Key.ctrl_r, keyboard.KeyCode(char='c')}
]

# The currently active modifiers
current = set()

tnow = datetime.datetime.now()
tcounter = 0

def on_press(key):
    if any([key in comb for comb in COMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in comb) for comb in COMBINATIONS):
            global tnow
            global tcounter
            tcounter += 1
            if datetime.datetime.now() - tnow < datetime.timedelta(seconds=1):
                if tcounter > 1:
                    tcounter = 0
                    main_function()
            else:
                tnow = datetime.datetime.now()
    if key == keyboard.Key.esc:
        listener.stop()


def on_release(key):
    try:
        current.remove(key)
    except KeyError:
        pass

def main_function():
    print('Main function fired!')
    # rest of your code here...

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()