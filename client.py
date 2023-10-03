'''This file contains my example TTS code, and how to use it'''
# INSTALL
#   First, you need vs build tools - https://visualstudio.microsoft.com/visual-cpp-build-tools/
#       the ui is crap but basically just click top left c++ box when all of the options appear
#   Then install with - pip install tts
#
#   some models require espeak - the one i use does...
#       download - https://github.com/espeak-ng/espeak-ng/releases/tag/1.51
#       then add to your path C:\Program Files\eSpeak NG\espeak-ng.exe
#       a restart is required
#       verify after by running in cmd - espeak-ng
#
#   We use VLC to play the sound, so install it and add it to your path!
#
#  Tweaked from - https://catid.io/posts/tts/
import subprocess, os, pyautogui, time, pyperclip
from pynput import keyboard












# do this 
'''This listents for ctrl +c pressed in under a second'''

## could be cool but anything with ctrl in does not work :(
#   perhaps look at https://github.com/moses-palmer/pynput/issues/20






































# The key combination to check
COMBINATIONS = [
    {keyboard.Key.shift, keyboard.KeyCode(char='q')},
    {keyboard.Key.shift, keyboard.KeyCode(char='Q')}
]
# The currently active modifiers
current = set()


def generate_voice_file(text:str):
    ''' This function generates a voice file from text given

        The voice variable changes the person speaking, list availible voices with:
            tts --model_name tts_models/en/vctk/vits --list_speaker_idxs
        The voice that is used 'p311' is a irish women with a slight accent

    '''
    voice = 'p311'
    command = 'tts --model_name tts_models/en/vctk/vits --text "' + text + '" --progress_bar True --speaker_idx ' + voice
    process = subprocess.Popen(command)
    process.wait()

def play_voice_file():
    ''' This function will play the voice file generated from generate_voice_file() using a headless vlc player

        It will also delete the generated tts_output.wav file after
    '''
    # If generate_voice_file() was able to create the voice:
    if os.path.isfile("tts_output.wav"):
        process = subprocess.Popen("vlc -I dummy --dummy-quiet tts_output.wav vlc://quit")
        process.wait()
        os.remove("tts_output.wav")
    else:
        print("we have problems...")
    

def stop_playback():
    # to stop playback we kill all vlc sessions
    # this function must be called from a seperate file/thread though
    subprocess.call("TASKKILL /F /IM vlc.exe", shell=True)
    

def get_selected_text():
    '''This function copies the selected text into the clipboard then returns it as a string

        It will clear the clipboard after 
    '''
    time.sleep
    pyautogui.keyDown('ctrl')
    pyautogui.press('c')
    pyautogui.keyUp('ctrl')
    data = pyperclip.paste()
    print(data)
    # We clear the clipboard
    #pyperclip.copy("")

    # If ''' is fed into generate_voice_file() the program will crash
    if "'''" not in data:
        generate_voice_file(text=data)



def on_press(key):
    '''When a key is pressed'''
    for combination in COMBINATIONS:
        if key in combination:
            current.add(key)
            if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
                # Any thing you want doing when the hotkey is pressed, goes here:
                get_selected_text()
                play_voice_file()

def on_release(key):
    '''When a key is released'''
    if any([key in COMBO for COMBO in COMBINATIONS]):
        ## Adding Try, except as heavy spam can cause crash
        try:
            current.remove(key)
        except KeyError:
            pass


if __name__ == "__main__":
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()









