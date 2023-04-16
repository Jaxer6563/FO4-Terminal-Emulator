# Module that allows for the program to determine what opperating system the user is using, and then clears the screen when called
from os import system, name


def clear():
    if name == 'nt' :   # For Windows
        _ = system('cls')
        
    else:   # For Unix systems
        _ = system('clear')
