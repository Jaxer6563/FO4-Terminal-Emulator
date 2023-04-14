# This module will create a cursor that can be moved around the terminal window to select text
from blessings import Terminal

t = Terminal()

print t.bold('Hi there')
print t.bold_red_on_bright_green('It hurts my eyes!')

with t.location(0, t.height - 1):
    print ('This is at the bottom")