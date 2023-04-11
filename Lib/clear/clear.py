# Import only system and name from os
from os import system, name

# Import sleep to show output for some time period
from time import sleep

# Define our clear function
def clear():
    if name == 'nt' :   # For Windows
        _ = system('cls')
        
    else:   # For Unix systems
        _ = system('clear')
