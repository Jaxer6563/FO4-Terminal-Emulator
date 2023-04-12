import time, sys
from Lib.typing import typing
from Lib.clear import clear
<<<<<<< Updated upstream
=======

FileName1 = " Tips\n\n"
FileName2 = " Chem Supplier Notes\n\n"
columns = shutil.get_terminal_size().columns
lines = shutil.get_terminal_size().lines
middle = int((lines / 2)-2)
cmiddle = int((columns/2)-15)

def loadingScreenTyping(delay):
    clear.clear()
    columns = shutil.get_terminal_size().columns
    lines = shutil.get_terminal_size().lines
    middle = int((lines / 2)-2)
    cmiddle = int((columns/2))
    print("WELCOME TO ROBCO INDUSTRIES (TM) TERMLINK")
    print("\n"*middle)
    print(" "*cmiddle)
    typing.typingPrintDelay("                                                                   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓", delay)

    

>>>>>>> Stashed changes
def startup():
    typing.typingPrint("\n\n> LOGON ADMIN")
    time.sleep(1)
    typing.typingPrint("\n\nENTER PASSWORD NOW")
    time.sleep(1)
    typing.typingPrint("\n\n>")
    time.sleep(2)
    typing.typingPrint(" ************")
    input()
    clear.clear()
    time.sleep(1)
<<<<<<< Updated upstream
    typing.typingPrintDelay("\n ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓",0.5)
=======
    loadingScreenTyping(0.5)
>>>>>>> Stashed changes
    time.sleep(1)
    clear.clear()
    
    
def home():
    print("WELCOME TO ROBCO INDUSTRIES (TM) TERMLINK\n")
    time.sleep(1)
    typing.typingPrint(FileName1)
    time.sleep(1)
    typing.typingPrint(FileName2 )
    time.sleep(1)
    input()

typing.typingPrint("WELCOME TO ROBCO INDUSTRIES (TM) TERMLINK")
FileName1 = "Tips\n\n"
FileName2 = "Chem Supplier Notes\n\n"

time.sleep(1)
startup()
home()