import random
import sys
import os

def logo():
    print('\t\t\t*********************************')
    print('\t\t\t*   CAN YOU GUESS THE COUNTRY?  *')
    print('\t\t\t*              Artemis 2020     *')
    print('\t\t\t*********************************')

listHint = [' '] * 57
for i in range(12):
    listHint[i] = 'Asia' 
for i in range(12, 28):
    listHint[i] = 'Europe'
for i in range(28, 38):
    listHint[i] = 'Africa'
for i in range(38, 47):
    listHint[i] = 'North America'
for i in range(47, 52):
    listHint[i] = 'South America'
for i in range(52, 57):
    listHint[i] = 'Oceania'

listHint2 = [line.strip() for line in open('Guess - Hint.txt')]
listCountries = [line.strip() for line in open('Guess - Country.txt')]

logo()
print('\nInstructions: Can you guess the country?, You are given a list of characters')
print('which is a random country name, you are tasked to guess the characters given')
print('or guess the country name in full, this game is a round of 3')
print('\nSo, Would you like to play?\n')
os.system('pause')

game, playerScore = 1, 0
while game < 4:
    os.system('cls')
    index = random.randrange(0, 58) # random index
    word = listCountries[index] #random choice of country
    finalWord = word.lower() # lowercased choice of country
    
    country = list(finalWord) #List version of chosen country
    temp = ['-']*len(country) # the print version
    guess = 3

    while guess > 0:
        os.system('cls')
        logo()
        print('Game: ', game, 'out of 3 ', 'Player Score: ', playerScore, '\n')
        for i in temp:
            print('[',i,']', end = ' ')
        
        print('\n   <<<<<Hints>>>>>\n-This Country is in', listHint[index], '\n-', end = '')
        print(listHint2[index])
    
        print('\nYou have ', guess, ' guess left')
        letter = input('Enter a Letter: ')
        if len(letter) > 1:
            if finalWord == letter.lower():
                print('\nWOAHHHH! You Guessed it right!\nThe Country really is: ', letter, '\n')
                playerScore += 1
                game += 1
                os.system('pause')
                os.system('cls')
                break
            else:
                print('\nOops! You are wrong!')
                guess -= 1
                if guess == 0:
                    print('The Country was: ', finalWord, '\n')
                    game += 1
                os.system('pause')
        else:
            a = 0
            for i in range(len(country)):
                if country[i] == letter.lower():
                    temp[i] = letter.lower()
                    if guess < 3:
                        guess += 1
                    else:
                        guess = 3
                    a = 1
                    os.system('cls')
            if a == 0:   
                print('\nOoops! You are wrong!')
                guess -= 1
                if guess == 0:
                    print('The Country was: ', finalWord, '\n')
                    game += 1
                os.system('pause')
                os.system('cls')
            word = ''.join(temp)
            if word == finalWord:
                print('\nYou Finally did it!\nThe Country really was: ', word, '\n')
                playerScore += 1
                game += 1
                os.system('pause')
                break
            continue
    if game == 4:
        print('\nPeww! You finished the Game with Score: ', playerScore)
        os.system('pause')
        sys.exit()
    else:
        continue
    
#ARTEMIS 04/01/20 Revised(v3)

