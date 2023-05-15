import time, sys, shutil, random, os
from Lib import typing_, clear, commands, hacking
os.system("mode con: cols=80    lines=25")
columns = shutil.get_terminal_size().columns
lines = shutil.get_terminal_size().lines
middle = int((lines / 2)-2)
cmiddle = int((columns/2)-15)

def loadingScreenTyping(delay):  # Gives a simple loading screen, taking an integer as the delay period.
    clear.clear()
    columns = shutil.get_terminal_size().columns
    lines = shutil.get_terminal_size().lines
    middle = int((lines / 2)-2)
    cmiddle = int((columns/2))
    print("WELCOME TO ROBCO INDUSTRIES (TM) TERMLINK")
    print("\n"*middle)
    print(" "*cmiddle)
    typing_.typingPrintDelay("                 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓", delay)
    time.sleep(delay*2)
    clear.clear()

def hackChance(): #
    num = random.randint(1,7) # Provides a 4 in 7 chance for the user to be required to try and figure out the password instead of the terminal starting up imediatly.
    if (num % 2) == 0:
        typing_.typingPrint("\n\n\nUnable to access login screen. Please enter Maintence Password to continue\n")
        input()
        hacking.crackPasscode()
    else:
        typing_.typingPrint("\n\n> LOGON ADMIN")
        time.sleep(1)
        typing_.typingPrint("\n\nENTER PASSWORD NOW")
        time.sleep(1)
        typing_.typingPrint("\n\n>")
        time.sleep(2)
        typing_.typingPrint(" ************")
        input()
    

def startup(): # Begins the entire program.
    
    hackChance()
    time.sleep(1)
    clear.clear()
    home()
    commands.commands()
    
      
def home(): # Sets up the entire program to begin running
    loadingScreenTyping(0.5)
    print("WELCOME TO ROBCO INDUSTRIES (TM) TERMLINK\n")
typing_.typingPrint(' ')
clear.clear()
os.chdir('Home/Users')
typing_.typingPrint("WELCOME TO ROBCO INDUSTRIES (TM) TERMLINK")
time.sleep(1)
startup()