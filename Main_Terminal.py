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
typing.typingPrint("WELCOME TO ROBCO INDUSTRIES (TM) TERMLINK")
time.sleep(1)
startup()
