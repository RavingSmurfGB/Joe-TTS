import pyperclip
 
# Read the text from the clipboard
text = pyperclip.paste()
pyperclip.copy("")
# Print the text
print(text)

