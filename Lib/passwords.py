from typing import List
import random as ran
wordlist = [] #type: List[str]
list = 'password.txt'
    
def getpassword(listofwords):
    f = open(list,'r')
    words = f.read()
    possibleWords = words.splitlines()
    
    indicies = ran.sample(range(1,40),28)
    for i in indicies:
        wordlist.append(possibleWords[i])
        
    return wordlist
    
    
    
getpassword(list)

