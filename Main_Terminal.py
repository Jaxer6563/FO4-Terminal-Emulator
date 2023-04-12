import time, sys
from Lib.typing import typing
from Lib.clear import clear
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
    print("WELCOME TO ROBCO INDUSTRIES (TM) TERMLINK")
    time.sleep(1)
    typing.typingPrintDelay("\n ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓",0.5)
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