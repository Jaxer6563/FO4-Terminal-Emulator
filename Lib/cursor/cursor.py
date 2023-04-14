# This module will create a cursor that can be moved around the terminal window to select text
from blessed import Terminal
import clear

term = Terminal()
print(term.home + term.clear + term.move_y(term.height // 2))
print(term.black_on_darkkhaki(term.center('press any key to continue.')))

with term.cbreak(), term.hidden_cursor():
    inp = term.inkey()

print(term.move_down(2) + 'You pressed ' + term.bold(repr(inp)))


def cursorBottomRight():
    clear.clear()
    print(term.height)
    print(term.width)
    input()
    clear.clear()
    print(term.home + term.clear + term.move(30,120))
    print(term.bold_blink_white_on_black+'▓')


cursorBottomRight()
input()

