#import time, sys, colorama, random
#from colorama import Fore, init, Back
from Lib import typing_

'''
typingPrint("Hello Stupid Humans \nYou are a stupid Human\n")
typingInput("How do you feel about being a stupid Human?\n")
typingPrint("FeelsBadMan")
'''
y="""You take the blue pill... the story ends, you wake up in your bed and believe whatever you want to believe.
You take the red pill... You stay in Wonderland, and I show you how deep the rabbit hole goes."""

typing_.typingPrint(y)
x = typing_.typingInput("\nYou can only take one. Choose Now\n")
if x == "Red":
    typing_.typingPrint("You are trapped in the Matrix forever")
    input()
elif x == "Blue":
    typing_.typingPrint("You have escaped the Matrix, and wake up in your bed")
    input()
elif x == "Both":
    typing_.typingPrint("You Moron.\n")
    time.sleep(2)
    typing_.typingPrint("You are dead...")
    input()
else:
    exit()

