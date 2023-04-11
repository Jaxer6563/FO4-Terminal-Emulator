import time, sys, colorama, random
from colorama import Fore, init, Back


init()

def sleeptime():
    interval = [ 0.15, 0.1, 0.05, 0.025]
    idx = random.randint(0,3)
    out = interval[idx]
    return out
    
def typingPrint(text):
    for character in text:
        sys.stdout.write(Fore.GREEN + Back.BLACK + character)
        sys.stdout.flush()
        time.sleep(0.05)

def typingInput(text):
    for character in text:
        sys.stdout.write(Fore.GREEN + Back.BLACK + character)
        sys.stdout.flush()
        time.sleep(0.05)
    value=input()
    return value
