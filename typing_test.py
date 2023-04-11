import time, sys, colorama, random
from colorama import Fore, init, Back
init()
def sleeptime():
    interval = [0.2, 0.15, 0.1, 0.05, 0.025]
    idx = random.randint(0,4)
    out = interval[idx]
    
    return out
    

def typingPrint(text):
    
    for character in text:
        sys.stdout.write(Fore.GREEN + Back.BLACK + character)
        sys.stdout.flush()
        time.sleep(sleeptime())

def typingInput(text):
    for character in text:
        sys.stdout.write(Fore.GREEN + Back.BLACK + character)
        sys.stdout.flush()
        time.sleep(sleeptime())
    value=input()
    return value

'''
typingPrint("Hello Stupid Humans \nYou are a stupid Human\n")
typingInput("How do you feel about being a stupid Human?\n")
typingPrint("FeelsBadMan")
'''
y="""You take the blue pill... the story ends, you wake up in your bed and believe whatever you want to believe.
You take the red pill... You stay in Wonderland, and I show you how deep the rabbit hole goes."""

typingPrint(y)
x = typingInput("\nYou can only take one. Choose Now\n")
if x == "Red":
    typingPrint("You are trapped in the Matrix forever")
    input()
elif x == "Blue":
    typingPrint("You have escaped the Matrix, and wake up in your bed")
    input()
elif x == "Both":
    typingPrint("You Moron.\n")
    time.sleep(2)
    typingPrint("You are dead...")
    input()
else:
    exit()

