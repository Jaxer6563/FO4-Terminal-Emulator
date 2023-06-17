import keyboard
import clear, typing_
list = 'passwords.txt'
def getWords():
    f = open(list,'r')
    words = f.read()
    possibleWords = words.splitlines()
    
    indicies = ran.sample(range(1,40),28)
    for i in indicies:
        wordlist.append(possibleWords[i])
        
    return wordlist
words = getWords()
while True:
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
    if keyboard.is_pressed("enter"):
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
        clear.clear()
        break
    