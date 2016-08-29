# Author: Nathan Calderon
# Filename: Well_Hello.py

# This is a guessing game. Guess a number between 1 and 20

import random   # import random module

print('Hello. What is your name?')
userName = input()

randNum = random.randint(1,20)
print('Well, ' + str(userName) + ' I am thinking of a number between 1 and 20.')
print('Take a pick, you have 6 attemps')
userNum = int(input())

guessCount = 1
condition = 6

while guessCount <= condition:
    if (int(userNum) == int(randNum)):
        print('Good job, ' + str(userName) + '! You guessed my number in ' + str(guessCount) + ' attempts')
        condition = 7
        break            
    else:
        print(str(condition-guessCount) + ' attempt(s) left, pick another')
        userNum = input()
        guessCount = guessCount + 1
        if ((guessCount == condition) and (int(userNum) != int(randNum))):
            print('It looks like you ran out of attemps hahahahahha')
    
