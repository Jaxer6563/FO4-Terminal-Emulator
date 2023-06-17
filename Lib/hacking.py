#This module adds a secondary login page, with the chance of accessing this page dependant on the hackchance() function in Main_Terminal.py
import os, shutil, time, random, keyboard
from Lib import typing_, clear, passwords
done = False

passwords.getWords(list)
time.sleep(.25)
password=passwords.getPassword()
time.sleep(.25)
passwords.setChars()
words = passwords.wordlist
    
def crackPasscode(): # Takes the hidden password, and prints out all possible password options.
                     # Then allows for input from the user to determine the password within 4 attempts.
                     # Otherwise the program kills its self and the user has to start again.
    clear.clear()
    global attempts
    attempts = 4
    while done == False:
        if attempts <=4 and attempts >0: # If the # of attempts is 4, then the program knows to use the typing_ module to print out each individual character
            passwordScreenHeader()
            print ('Attempts Left: '+'▓ '*attempts+'\n')
            possiblePasswords()
            if attempts == 1:
                print ('Warning! Lock-Out Iminent')
        elif attempts == 0:
            print('No More Attempts. Lockout Initiated')
            exit()
        passwordInput = input("Enter the Maintence Password to Continue: ")

        if passwordInput == password:
            typing_.typingPrintDelay('Success!',0.125)
            break
        elif passwordInput == 'REVEAL PASSWORD':
            clear.clear()
            typing_.typingPrintDelay(password+'\n',0.125)
            time.sleep(1)
            clear.clear()   
        elif passwordInput == None:
            pass
        else:
            typing_.typingPrintDelay('Invalid Password. Try again',0.125)
            attempts = attempts -1
            clear.clear()
            
    
def passwordScreenHeader():
    typing_.typingPrint("WELCOME TO ROBCO INDUSTRIES (TM) TERMLINK\n\n")
    typing_.typingPrint('Password Required\n\n')

def possiblePasswords():   
    
    try:
        typing_.typingPrintDelay('0xCC01 |'+words[0]+' |0xCC02 |'+words[1]+'\n',.1)
        typing_.typingPrintDelay('0xCC03 |'+words[2]+' |0xCC04 |'+words[3]+'\n',.1)
        typing_.typingPrintDelay('0xCC05 |'+words[4]+' |0xCC06 |'+words[5]+'\n',.1)
        typing_.typingPrintDelay('0xCC07 |'+words[6]+' |0xCC08 |'+words[7]+'\n',.1)
        typing_.typingPrintDelay('0xCC09 |'+words[8]+' |0xCC10 |'+words[9]+'\n',.1)
        typing_.typingPrintDelay('0xCC11 |'+words[10]+' |0xCC12 |'+words[11]+'\n',.1)
        typing_.typingPrintDelay('0xCC13 |'+words[12]+' |0xCC14 |'+words[13]+'\n',.1)
        typing_.typingPrintDelay('0xCC15 |'+words[14]+' |0xCC16 |'+words[15]+'\n',.1)
        typing_.typingPrintDelay('0xCC17 |'+words[16]+' |0xCC18 |'+words[17]+'\n',.1)
        typing_.typingPrintDelay('0xCC19 |'+words[18]+' |0xCC20 |'+words[19]+'\n',.1)
        typing_.typingPrintDelay('0xCC21 |'+words[20]+' |0xCC22 |'+words[21]+'\n',.1)
        typing_.typingPrintDelay('0xCC23 |'+words[22]+' |0xCC24 |'+words[23]+'\n',.1)
        typing_.typingPrintDelay('0xCC25 |'+words[24]+' |0xCC26 |'+words[25]+'\n',.1)
        typing_.typingPrintDelay('0xCC27 |'+words[26]+' |0xCC28 |'+words[27]+'\n',.1)
    except KeyboardInterrupt:
        clear.clear()
        print("WELCOME TO ROBCO INDUSTRIES (TM) TERMLINK\n\n")
        print('Password Required\n\n')
        print('Attempts Left: '+'▓ '*attempts+'\n')
        if attempts == 1:
                print ('Warning! Lock-Out Iminent')
        print('0xCC01 |'+words[0]+' |0xCC02 |'+words[1])
        print('0xCC03 |'+words[2]+' |0xCC04 |'+words[3])
        print('0xCC05 |'+words[4]+' |0xCC06 |'+words[5])
        print('0xCC07 |'+words[6]+' |0xCC08 |'+words[7])
        print('0xCC09 |'+words[8]+' |0xCC10 |'+words[9])
        print('0xCC11 |'+words[10]+' |0xCC12 |'+words[11])
        print('0xCC13 |'+words[12]+' |0xCC14 |'+words[13])
        print('0xCC15 |'+words[14]+' |0xCC16 |'+words[15])
        print('0xCC17 |'+words[16]+' |0xCC18 |'+words[17])
        print('0xCC19 |'+words[18]+' |0xCC20 |'+words[19])
        print('0xCC21 |'+words[20]+' |0xCC22 |'+words[21])
        print('0xCC23 |'+words[22]+' |0xCC24 |'+words[23])
        print('0xCC25 |'+words[24]+' |0xCC26 |'+words[25])
        print('0xCC27 |'+words[26]+' |0xCC28 |'+words[27])

#crackPasscode()