import random
import sys
import os

number = random.randrange(1, 101)
randomBasis = random.randrange(1, 100)

guess = 5
while guess > 0:
    os.system('cls')
    print('\nGuess the Number! 1-100')
    if number > randomBasis:
        print('The Number is greater than', randomBasis)
    else:
        print('The Number is less than', randomBasis)
    
    print('\nGuess Left: ', guess)
    player = int(input('Enter your Guess: '))
    if player == number:
        guess += 1
        print('Nice! You did it after', 5 - guess, ' tries')
        sys.exit()
    else:
        if player > number and player <= number + 5 or player > number and player >= number - 5:
            print('\nOoops! You are too close to guessing it')
            if player > number:
                print('Lower!!\n')
            else:
                print('Higher!!\n')
        else:
            print('\nOoops! You are too far to guessing it!')
            if player > number:
                print('Lower!!\n')
            else:
                print('Higher!!\n')
        guess -= 1
        os.system('pause')
        continue
print('\nYou Lost! The Number is: ', number)
os.system('pause')
sys.exit()
#ARTEMIS - 03/31/20
