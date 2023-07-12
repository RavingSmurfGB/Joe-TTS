import pyttsx3
# pip install pyttsx3
# not continuing with thos module - I did not like the voice


engine = pyttsx3.init()

engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()