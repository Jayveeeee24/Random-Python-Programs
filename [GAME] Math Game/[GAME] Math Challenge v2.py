import random
import sys
import os

def logo():
    print('\t\t\t*************************************')
    print('\t\t\t*     Math Challenge v2: Battle     *')
    print('\t\t\t*                  Artemis 2020     *')
    print('\t\t\t*************************************')

playerHealth = 200
compHealth = 500

saying = ['You suck at maths dimwit!', 'Are you stupid?',
          'Can\'t you even make that right?',
          'How pathetic of you! Human', 'Is this all you got?', 'You are such a weakling',
          'I never thought you would be this stupid!']

logo()
print('\nElder: A Monster appeared out of Nowhere!',
      '\nThe Monster wants to destroy our village!',
      '\nIt challenges you to fight him in a math challenge',
      '\nThere\'s no turning back now!, ',
      '\n\nPrincess: You have to fight him and save our village!\n')
os.system('pause')
def check():
    if playerHealth <= 0 or compHealth <= 0:
        if compHealth <= 0:
            print('\nElder: You save us! Our bravest soldier!')
            print('Princess: Thank you for saving us!')
            print('\nMonster: I will definitely defeat you someday!')
        elif playerHealth <= 0:
            print('\nMonster: HAHA YOU LOST WEAKLING! YOU CANT DEFEAT ME!')
            print('Elder: Oh noooo! We lost and our village will be destroyed!')
        sys.exit()
    
while compHealth > 0 or playerHealth > 0:
    os.system('cls')
    logo()
    print('Boss Health: ', compHealth)
    print('Player\'s Health: ', playerHealth)
    operator = random.randrange(1, 5)
    number1 = random.randrange(1, 100)
    number2 = random.randrange(1, 100)

    if operator == 1:
        print('\nThe problem is: ', number1, ' + ', number2)
        val = int(input('Your Answer: '))
        if val == number1 + number2:
            print('\nMonster have suffered ', number1 + number2, ' damage')
            print('Elder: Nice! You are great!')
            compHealth = compHealth - (number1 + number2)
            check()
            print('\n')
            os.system('pause')
            continue
        else:
            print('\nYou have suffered ', number1 + number2, ' damage')
            print('Monster: ', random.choice(saying))
            print('The answer is: ', number1 + number2)
            playerHealth = playerHealth - (number1 + number2)
            check()
            print('\n')
            os.system('pause')
            continue
    elif operator == 2:
        if number2 > number1:
            number1 = random.randrange(50, 100)
            number2 = random.randrange(1, 50)
        print('\nThe problem is: ', number1, ' - ', number2)
        val = int(input('Your Answer: '))
        if val == number1 - number2:
            print('\nMonster have suffered ', number1 - number2, ' damage')
            print('Princess: You are great warrior!')
            compHealth = compHealth - (number1 - number2)
            check()
            print('\n')
            os.system('pause')
            continue
        else:
            print('\nYou have suffered ', number1 - number2, ' damage')
            print('Monster: ', random.choice(saying))
            print('The answer is: ', number1 - number2)
            playerHealth = playerHealth - (number1 - number2)
            check()
            print('\n')
            os.system('pause')
            continue
    elif operator == 3:
        number1 = random.randrange(1, 20)
        number2 = random.randrange(1, 25)
        print('\nThe problem is: ', number1, ' * ', number2)
        val = int(input('Your Answer: '))
        if val == number1 * number2:
            print('\nMonster have suffered ', number1 * number2, ' damage')
            print('Elder: You got it right!')
            compHealth = compHealth - (number1 * number2)
            check()
            print('\n')
            os.system('pause')
            continue
        else:
            print('\nYou have suffered ', number1 * number2, ' damage')
            print('Monster: ', random.choice(saying))
            print('The answer is: ', number1 * number2)
            playerHealth = playerHealth - (number1 * number2)
            check()
            print('\n')
            os.system('pause')
            continue
    elif operator == 4:
        if number2 > number1:
            number1 = random.randrange(50, 100)
            number2 = random.randrange(1, 50)
        print('\nThe problem is: ', number1, ' / ', number2)
        val = int(input('Your Answer: '))
        if val == number1 // number2:
            print('\nMonster have suffered ', number1 // number2, ' massive damage')
            print('Princess: You are a hero!')
            compHealth = compHealth - number1 // number2
            check()
            print('\n')
            os.system('pause')
            continue
        else:
            print('\nYou have suffered ', number1 // number2, ' massive damage')
            print('Monster: ', random.choice(saying))
            print('The answer is: ', number1 // number2)
            playerHealth = playerHealth - number1 // number2
            check()
            print('\n')
            os.system('pause')
            continue
os.system('pause')


#ARTEMIS - 03/31/20
