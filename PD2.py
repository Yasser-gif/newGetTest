import os
import sys
import time
import random
with open('wordbank.txt','r') as wb:
    word_b = [line.rstrip('\n') for line in wb]
pr=open("PlayersRecords.txt","a+")
tword=random.choice(word_b)
print tword
word=list(tword)
print word
letnum=len(word)
print letnum
Hidd=[]
LTRS=set()
results=[]
result=[]
for i in range(letnum):
    Hidd.append('-')
print Hidd
wrong_g=0
Name=raw_input("Please enter your name: ")
print ("        *****Welcome to the Hangman Game*****")
print ("1. Player will guess a letter to find the random word.")
print ("2. Each wrong guess will be counted.")
print ("3. After reaching 7 (seven) wrong guesses, the game will be over.")
print ("4. The game will won only if the players guesses all the letters in the random word correctly.")
if os.stat("PlayersRecords.txt").st_size==0:
    print "There are no previous players."
else:
    results=[line.rstrip('\n') for line in pr.readlines()]
    print "Best five results:"
    print "Name"+"          "+"Elapsed Time"+"         "+"Wrong Guesses"
    for i in range(5):
        print results[i]
raw_input("Please press 'Enter' to start")
start_t=time.time()
print "The word hidden is:",'\n', ' '.join(Hidd)
while wrong_g != 7:
    print "Chosen letters until now: "
    if not(LTRS):
        print "No chosen letters"
    else:
        print ' '.join(LTRS)
    Lett=raw_input("Please enter a letter (in lowercase): ")
    Lett=Lett.lower()
    while not(Lett.isalpha()):
        print "Invalid choice"
        Lett=raw_input("Please enter a valid character (in lowercase): ")
        Lett=Lett.lower()
    while Lett in LTRS:
        print "Letter already inputted"
        Lett=raw_input("Please enter another letter (in lowercase): ")
        Lett=Lett.lower()
    if Lett not in word:
        wrong_g=wrong_g+1
        print "Wrong guess. Letter not included"
    else:
        num=word.count(Lett)
        letnum=letnum-num
        print "Correct guess. Letter included"
        for i in range(len(word)):
            if Lett==word[i]:
                Hidd[i]=Lett
                LTRS.add(Lett)
        print ' '.join(Hidd)
        if letnum==0:
            end_t=time.time()
            elapsed_t=end_t-start_t
            print "Congratulations. YOU WON!"
            print "The number of wrong guesses is: ",wrong_g
            print "Time spent: ", elapsed_t
            Res=(Name,wrong_g,elapsed_t)
            result.append(Res)
            for line in pr.readlines():
                tem=line.split()
                result.append((tem[0],float(tem[1]),float(tem[2]))
            result=sorted(result,key=lambda j:(j[1],j[2]),reverse=True)
            pr.write('\n'.join('%s          %s          %s' %y for y in result)
            sys.exit(0)
print "You Lost the game. Nice try"
print "The word was: ", tword    
pr.close()

