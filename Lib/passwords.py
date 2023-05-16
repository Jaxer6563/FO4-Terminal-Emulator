import random as ran
wordlist = []
f = open('password.txt', 'r')
words = f.read()
possiblewords = words.splitlines()
alreadyUsed=[]
for i in range(28):
    while True:
    index = randint(0,27)
    if index in alreadyUsed:
        break
    else:
        alreadyUsed.append(index)
        wordlist.append(possibleWords[index])
        print (wordlist[index])
    
    