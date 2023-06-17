from typing import List
import random as ran
import string, time
wordlist = [] #type: List[str]
list = 'Lib/password.txt'


def getWords(listofwords):
    f = open(list,'r')
    words = f.read()
    possibleWords = words.splitlines()
    
    indicies = ran.sample(range(1,40),28)
    for i in indicies:
        wordlist.append(possibleWords[i])
        
    return wordlist
    

def getPassword():
    password = ran.choice(wordlist)
    return password
def setChars():
    for i in range(len(wordlist)):
        random_string=''.join(ran.choices(string.punctuation, k=12))
        left = (len(random_string) - len(wordlist[i])) // 2
        right = left + len(wordlist[i])
        padded_word = random_string[:left] + wordlist[i] + random_string[right:]
        wordlist[i] = padded_word
    return wordlist


    

'''
getWords(list)

time.sleep(.25)
password=getPassword()
time.sleep(.25)
setChars()
print (password+'\n\n\n')
for i in range(len(wordlist)):
    print(wordlist[i])
    '''