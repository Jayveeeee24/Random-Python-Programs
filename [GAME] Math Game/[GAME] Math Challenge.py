import random
from random import randrange
playerScore = 0
counter = 0
    

while counter < 10:
    print('\nMath Challenge!\nPlayer Score :', playerScore)
    operator = random.randrange(1, 5)
    number1 = random.randrange(1, 100)   
    number2 = random.randrange(1, 100)

    if operator == 1:
        print('Problem: ', number1, ' + ', number2)
        val = int(input('Your Answer: '))
        if val == number1 + number2:
            print('Nice! You are Genius!')
            counter = counter + 1
            playerScore = playerScore + 1
            continue
        else:
            print('Ooop! You\'re Wrong! The answer is: ', number1 + number2)
            counter += 1
            continue
    elif operator == 2:
        if number2 > number1:
            number1 = random.randrange(50, 101)
            number2 = random.randrange(1, 51)
        else:
            print('Problem: ', number1, ' - ', number2)
            val = int(input('Your Answer; '))
            if val == number1 - number2:
                print('Nice You are Genius!')
                counter = counter + 1
                playerScore += 1
                continue
            else:
                print('Ooop! You\'re Wrong! The answer is: ', number1 - number2)
                counter += 1
                continue
    elif operator == 3:
        number1 = random.randrange(1, 40)
        number2 = random.randrange(1, 20)
        print('Problem: ', number1, ' * ', number2)
        val = int(input('Your Answer: '))
        if val == number1 * number2:
            print('Nice You are Genius!')
            counter += 1
            playerScore += 1
            continue
        else:
            print('Ooop! You\'re Wrong! The answer is: ', number1 * number2)
            counter += 1
            continue
    elif operator == 4:
        if number2 > number1:
            number1 = random.randrange(40, 101)
            number2 = random.randrange(1, 21)
        print('Problem: ', number1, ' / ', number2)
        val = int(input('Your Answer: '))
        if val == number1 // number2:
            print('Nice You are Genius!')
            counter = counter + 1
            playerScore += 1
            continue
        else:
            print('Ooop! You\'re Wrong! The answer is: ', number1 // number2)
            counter += 1
            continue

print('\n')
if playerScore == 10:
    print('Woaaaaahh! You are a real Genius!\nScore: ', playerScore, '/10 Mistakes: ', 10 - playerScore)
elif playerScore > 6 and playerScore < 10:
    print('Wow! Nice You are pretty Smart!\nScore: ', playerScore, '/10 Mistakes: ', 10 - playerScore) 
elif playerScore >= 5 and playerScore <= 6:
    print('Still Great! You scored average\nScore: ', playerScore, '/10 Mistakes: ', 10 - playerScore)
else:
    print('Better Luck Next Time!\nScore: ', playerScore, '/10 Mistakes: ', 10 - playerScore)
          
#ARTEMIS - 03/29/20
