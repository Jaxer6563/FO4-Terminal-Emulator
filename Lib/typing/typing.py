import time, sys, colorama, random
from colorama import Fore, init, Back, Style


init()

def sleeptime(): # Randomlly decides the delay for that of the typingPrint and typingInput functions so they mimic an actual person typing at variable speeds
    interval = [ 0.15, 0.1, 0.05, 0.025]
    idx = random.randint(0,3)
    out = interval[idx]
    return out
    
def typingPrint(text): # Has a delay between individual characters appearing on the screen
    for character in text:
        if character == " ":
            sys.stdout.write(Fore.GREEN + Back.BLACK + Style.BRIGHT + character)
            sys.stdout.flush()
        else:
            sys.stdout.write(Fore.GREEN + Back.BLACK + Style.BRIGHT + character)
            sys.stdout.flush()
            time.sleep(sleeptime())

def typingInput(text): # Has a delay between individual characters appearing on the screen
    for character in text:
        if character == " ":
            sys.stdout.write(Fore.GREEN + Back.BLACK + Style.BRIGHT + character)
            sys.stdout.flush()
        else:
            sys.stdout.write(Fore.GREEN + Back.BLACK + Style.BRIGHT + character)
            sys.stdout.flush()
            time.sleep(sleeptime())
    value=input()
    return value

def typingPrintDelay(text, delay): # Version of typingPrint() that allows user to specify the duration of the delay between keystrokes
    for character in text:
        if character == " ":
            sys.stdout.write(Fore.GREEN + Back.BLACK + Style.BRIGHT + character)
            sys.stdout.flush()
        else:
            sys.stdout.write(Fore.GREEN + Back.BLACK + Style.BRIGHT + character)
            sys.stdout.flush()
            time.sleep(sleeptime())