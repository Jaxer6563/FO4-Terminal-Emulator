import os, shutil, time
from Lib import typing_, clear
done = False
words = ['MARKS','EMPTY','ENACT','SWORE','HELPS','KNOWS','STAKE','LARGE','UNITE','STARK','TORCH','HANDY','TRACK','DAILY','CLOCK','GLASS','SEIZE','SLING','REFER','FLAME','HOMES','WOULD','SMALL','APTLY','THESE','FAULT','GOODS']
import random
def choosePassword():
    global password
    password = random.choice(words)
    
def crackPasscode():

    clear.clear()
    choosePassword()
    attempts = 4
    while done == False:
        passwordScreenHeader()
        if attempts == 4:
            typing_.typingPrintDelay('Attempts Left: ▓ ▓ ▓ ▓\n\n',0.125)
            possiblePasswords()
        elif attempts == 3:
            typing_.typingPrintDelay('Attempts Left: ▓ ▓ ▓\n\n',0.125)
            possiblePasswords()
        elif attempts == 2:
            typing_.typingPrintDelay('Attempts Left: ▓ ▓\n\n',0.125)
            possiblePasswords()
        elif attempts == 1:
            typing_.typingPrintDelay('Attempts Left: ▓  - Lockout Imminent\n\n',0.125)
            possiblePasswords()
        elif attempts == 0:
            typing_.typingPrintDelay('No More Attempts. Lockout Initiated',0.125)
            exit()
        
        passwordInput = typing_.typingInput("Enter the Maintence Password to Continue: ")
        if passwordInput == password:
            typing_.typingPrintDelay('Success!',0.125)
            break
        elif passwordInput == 'REVEAL PASSWORD':
            typing_.typingPrintDelay(password+'\n',0.125)
            clear.clear()
        else:
            typing_.typingPrintDelay('Invalid Password. Try again',0.125)
            attempts = attempts -1
            clear.clear()
            
    
def passwordScreenHeader():
    print("WELCOME TO ROBCO INDUSTRIES (TM) TERMLINK\n\n")
    typing_.typingPrint('Password Required\n\n')

def possiblePasswords():
    print('0xCC01 |{)&@*'+words[0]+'@ |0xCC02 |!(#'+words[1]+'@)!#')
    print('0xCC03 |[#%'+words[2]+'+(! |0xCC04 |!*#'+words[3]+'!)&$')
    print('0xCC05 |'+words[4]+'*@)>$_ |0xCC06 |!@*$'+words[5]+'!)&#')
    print('0xCC07 |)>}!#$'+words[6]+' |0xCC08 |!(#$'+words[7]+')(^#')
    print('0xCC09 |)!>}'+words[8]+'@& |0xCC10 |!*#('+words[9]+'!)&;')
    print('0xCC11 |)!&'+words[10]+')@# |0xCC12 |*#)'+words[11]+'[)!^')
    print('0xCC13 |!&<'+words[12]+')>! |0xCC14 |(!)'+words[13]+'>!&#')
    print('0xCC15 |[()!>)'+words[14]+' |0xCC16 |#&$'+words[15]+')!^#')
    print('0xCC17 |&@'+words[16]+'*(@! |0xCC18 |@&!)$'+words[17]+')!<%')
    print('0xCC19 |<()'+words[18]+'^#* |0xCC20 |!)@#'+words[19]+'>)!&')
    print('0xCC21 |!&#'+words[20]+'&@* |0xCC22 |!($'+words[21]+'!*$>')
    print('0xCC23 |&@)$'+words[22]+'   |0xCC24 |!&$#'+words[23]+')<!"')
    print('0xCC25 |@(4}'+words[24]+'   |0xCC26 |)@*#'+words[25]+'(!>$')
    print('0xCC27 |[*$(#'+words[26]+'  |0xCC28 |!&#FISHY&#(')
    
    passwordScreenHeader()
    if attempts == 4:
        print('Attempts Left: ▓ ▓ ▓ ▓\n\n')
        possiblePasswords()
    elif attempts == 3:
        print('Attempts Left: ▓ ▓ ▓\n\n')
        possiblePasswords()
    elif attempts == 2:
        print('Attempts Left: ▓ ▓\n\n')
        possiblePasswords()
    elif attempts == 1:
        print('Attempts Left: ▓\n\n')
        possiblePasswords()
    
    
def passwordScreenHeader():
    print("WELCOME TO ROBCO INDUSTRIES (TM) TERMLINK\n\n")
    print('Password Required\n\n')

def possiblePasswords():
    print('0xCC01  |{)&@*'+words[0]+'@ |0xCC02 |!(#'+words[1]+'@)!#')
    print('0xCC03  |[#%'+words[2]+'+(! |0xCC04 |!*#'+words[3]+'!)&$')
    print('0xCC05  |'+words[4]+'*@)>$_ |0xCC06 |!@*$'+words[5]+'!)&#')
    print('0xCC07  |)>}!#$'+words[6]+' |0xCC08 |!(#$'+words[7]+')(^#')
    print('0xCC09  |)!>}'+words[8]+'@& |0xCC10 |!*#('+words[9]+'!)&;')
    print('0xCC011 |)!&'+words[10]+')@# |0xCC12 |*#)'+words[11]+'[)!^')
    print('0xCC011 |!&<'+words[12]+')>! |0xCC14 |(!)'+words[13]+'>!&#')
    print('0xCC011 |[()!>)'+words[14]+' |0xCC16 |#&$'+words[15]+')!^#')
    print('0xCC011 |&@'+words[16]+'*(@! |0xCC18 |@&!)$'+words[17]+')!<%')
    print('0xCC011 |<()'+words[18]+'^#* |0xCC20 |!)@#'+words[19]+'>)!&')
    print('0xCC011 |!&#'+words[20]+'&@* |0xCC22 |!($'+words[21]+'!*$>')
    print('0xCC011 |&@)$'+words[22]+'   |0xCC24 |!&$#'+words[23]+')<!"')
    print('0xCC011 |@(4}'+words[24]+'   |0xCC26 |)@*#'+words[25]+'(!>$')
    print('0xCC011 |[*$(#'+words[26]+'  |0xCC28 |!&#FISHY&#(')
