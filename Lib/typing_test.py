import time, sys

def typingPrint(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

def typingInput(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    value=input()
    return value


typingPrint("Hello Stupid Humans \nYou are a stupid Human\n")
typingInput("How do you feel about being a stupid Human?\n")
typingPrint("FeelsBadMan")

