import time, sys, shutil, random
from Lib import typing, clear, fileModification

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
    typing.typingPrintDelay("                                                   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓", delay)
    time.sleep(delay*2)
    clear.clear()

def hackChance():
    num = random.randint(1,7)
    if (num % 2) == 0:
        typing.typingPrint("\n\n\nUnable to access login screen. Please enter Maintence Password to continue\n")
        input()
    else:
        typing.typingPrint("\n\n> LOGON ADMIN")
        time.sleep(1)
        typing.typingPrint("\n\nENTER PASSWORD NOW")
        time.sleep(1)
        typing.typingPrint("\n\n>")
        time.sleep(2)
        typing.typingPrint(" ************")
        input()
    

def startup():
    hackChance()
    time.sleep(1)
    clear.clear()
    
      
def home():
    loadingScreenTyping(0.5)
    print("WELCOME TO ROBCO INDUSTRIES (TM) TERMLINK\n")
    time.sleep(1)
    typing.typingPrint(">" + FileName1)
    time.sleep(1)
    typing.typingPrint(">" + FileName2 )
    time.sleep(1)
    
typing.typingPrint("WELCOME TO ROBCO INDUSTRIES (TM) TERMLINK")
time.sleep(1)
startup()
home()
fileModification.commands()