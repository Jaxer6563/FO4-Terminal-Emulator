import time, sys

def typingPrint(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.1)

def typingInput(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.1)
    value=input()
    return value

###
#typingPrint("Hello Stupid Humans \nYou are a stupid Human\n")
#typingInput("How do you feel about being a stupid Human?\n")
#typingPrint("FeelsBadMan")

###
typingPrint("You take the blue pill... the story ends, you wake up in your bed and beleive whatever you want to believe.")