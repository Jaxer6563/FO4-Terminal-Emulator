import time, sys, colorama
from colorama import Fore, init, Back
init()
def typingPrint(text):
    for character in text:
        sys.stdout.write(Fore.BLACK + Back.GREEN + character)
        sys.stdout.flush()
        time.sleep(0.05)

def typingInput(text):
    for character in text:
        sys.stdout.write(Fore.BLACK + Back.GREEN + character)
        sys.stdout.flush()
        time.sleep(0.05)
    value=input()
    return value


typingPrint("Hello Stupid Humans \nYou are a stupid Human\n")
typingInput("How do you feel about being a stupid Human?\n")
typingPrint("FeelsBadMan")


#typingPrint("You take the blue pill... the story ends, you wake up in your bed and believe whatever you want to believe. \nYou take the red pill... You stay in Wonderland, and I show you how deep the rabbit hole goes.")

