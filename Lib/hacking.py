#Password cracking portion of the FO4-Terminal-Emulator

attempts = 4



words = ['MARKS','EMPTY','ENACT','SWORE','HELPS','KNOWS','STAKE','LARGE','UNITE','STARK','TORCH','HANDY','TRACK','DAILY','CLOCK','GLASS','SEIZE','SLING','REFER','FLAME','HOMES','WOULD','SMALL','APTLY','THESE','FAULT','GOODS']
import random
def choosePassword():
    global password
    password = random.choice(words)
    
def crackPasscode():
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
    
    
choosePassword()
crackPasscode()
