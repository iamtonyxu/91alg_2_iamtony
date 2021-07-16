#! python3
# bulletPointAdder.py - Adds bullet points to the start
# of each line of text in clipboard
import pyperclip

text = pyperclip.paste()

# Seperate lines and add stars
lines = text.split('\n')
text = ''
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]
    #text += lines[i] # Wrong. There is no '\n' among lines

text = '\n'.join(lines)

pyperclip.copy(text)