#Challenge No. 1
########################################
#This program is a Rock, Paper and Scissors Game
########################################
import random
import os

game = 0
playerScore, computerScore = 0, 0
name1, name2 = '', ''

print('Welcome to JakEnPoy')

while game < 3:
    print('\n[1]. Rock\n[2]. Paper\n[3]. Scissors')
    player = int(input('Choice: '))
    computer = random.randrange(1,3)
    if player < 1:
        print('Invalid Input! Please Try again!')
        continue
    if player == computer:
        print('\nThe game is drawn!')
        continue
    if player == 1:
        name1 = 'Rock'
        if computer == 2:
            name2 = 'Paper'
            computerScore +=1
            game +=1
            print('You: ', name1, '\nComputer: ', name2)
            print('Computer Won!')
            continue
        if computer == 3:
            name2 = 'Scissors'
            playerScore +=1
            game +=1
            print('You: ', name1, '\nComputer: ', name2)
            print('Player Won!')
            continue
    
    if player == 2:
        name1 = 'Paper'
        if computer == 1:
            name2 = 'Rock'
            playerScore +=1
            game +=1
            print('You: ', name1, '\nComputer: ', name2)
            print('Player Won!')
            continue
        if computer == 3:
            name2 = 'Scissors'
            computerScore +=1
            game +=1
            print('You: ', name1, '\nComputer: ', name2)
            print('Computer Won!')
            continue

    if player == 3:
        name1 = 'Scissors'
        if computer == 1:
            name2 = 'Rock'
            computerScore +=1
            game +=1
            print('You: ', name1, '\nComputer: ', name2)
            print('Computer Won!')
            continue
        if computer == 2:
            name2 = 'Paper'
            playerScore +=1
            game +=1
            print('You: ', name1, '\nComputer: ', name2)
            print('Player Won!')
            continue

print('\n\n\n')
if playerScore > computerScore:
    print('Nice!, You Won!\nPlayer: ', playerScore, ' vs Computer: ', computerScore) 
else:
    print('HAHA!, You Lost!\nPlayer: ', playerScore, ' vs Computer: ', computerScore)


#ARTEMIS - 03/28/20




