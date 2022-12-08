import random
import os
import sys
import time

def logo():
    print('\t\t\t*************************************') 
    print('\t\t\t*          Typing Master            *')
    print('\t\t\t*                  Artemis 2020     *')
    print('\t\t\t*************************************')



#this is the original list of all records
list_allScores = [line.strip() for line in open('TypingMaster - Records.txt')]
#do the original haraters ake ore shaodnws like life sized with a liking to a nothherhdo you anoterhhh

#this will contain all splitted records into multidimensional array [[name, time, etc...], [name, time, etc...]]
splittedScores = [line.split() for line in list_allScores]

#this will serve as the containers for sum of all time and its indices
list_sumScores = [] #this is for the container of the total time
listIndices = [] # this is for its indices



#here it gets all total time in the [i][2] index where the [i] is the index of the individual record (EXAMPLE [array(0)[name(0), time(1), etc...], array(1)[name(0), time(1), etc...]]
for i in range(len(splittedScores)):
    if splittedScores[i][4] == '10': #here, if the splittedScore[i][4], where [4] is the index of the scores, it must equal to ten for it to be a high score
        list_sumScores.append(float(splittedScores[i][1])) #here it adds the record of all the time which is in the index [1]
        listIndices.append(i)#here it adds the index

lowestTime = min(list_sumScores)#this is the conversion of the minimun total time
index = []

index.append(list_sumScores.index(lowestTime))#here it gets the index of the lowest time and adds it to the list in index [0]
index.append(listIndices[index[0]])#this is the index of the lowest time - [1]

string = list_allScores[index[1]] #this gets the unsplitted record of the high score
information = string.split() # here it splits the record

#breaks down to all the variables
Name = information[0]
totalTime = information[1]
fastest = information[2]
slowest = information[3]

while True:
    logo()
    print('\n\nCan You Type as fast as the latest record?\n')
    print('Name: ', Name, ' Time: ', totalTime, 'seconds')
    print('Fastest: ', fastest, 'seconds\nSlowest: ', slowest, 'seconds')
    print('\n')
    print('NOTE: PLEASE DO NOT INCLUDE SPACE IN YOUR NAME!')
    name = input('Enter your Name: ')
    if ' ' in name or '\t' in name or '\n' in name or name == '':
        print('INVALID NAME! PLEASE TRY AGAIN!')
        os.system('pause')
        os.system('cls')
        continue
    else:
        break
print('\n')

listWord = [line.strip() for line in open('TypingMaster - Words.txt')]
os.system('pause')

listTime = []
list_playerWords = []
listMistakes = []
list_mistakenInput = []
score, game = 0, 0
while game < 10:
    word = listWord[random.randrange(0, len(listWord))]
    list_playerWords.append(word)
    os.system('cls')
    logo()
    start = time.time()
    print('NOTE: DO NOT WORRY ABOUT LETTERCASES')
    print('\nType this word: ', word.lower())
    userWord = input('\nEnter Word: ')
    
    if word.lower() == userWord.lower():
        timeEnd = time.time() - start
        score += 1
        print('\nGAME: ', game+1, ' SCORE: ', score)
        print('YOU DID IT! ', name,'- Ready for the next!')
        game += 1
        print('\nTIME: ', round(timeEnd,2), 'seconds')
        listTime.append(round(timeEnd, 2))
        print('Unofficial Total Time: ', round(sum(listTime), 2), 'seconds\n')
        os.system('pause')
        continue
    else:
        timeEnd = time.time() - start
        print('\nGAME: ', game+1, ' SCORE: ', score)
        print('Ooops! YOU ARE WRONG! ', name,'! - Brace yourself\n\nTIME: ', round(timeEnd,2), 'seconds')
        game += 1
        listMistakes.append(word)
        list_mistakenInput.append(userWord)
        listTime.append(round(timeEnd, 2))
        print('Unofficial Total Time: ', round(sum(listTime), 2), 'seconds\n')
        os.system('pause')
        continue

timeSum = round(sum(listTime), 2)
os.system('cls')
if timeSum < lowestTime and score == 10:
    print('Woah!! You set a high score!!')
print('\nPew!', name,' you finished the Challenge!\nScore:', score,' Mistakes: ', 10-score,'\nTotal time: ', timeSum, 'seconds')
fastest = round(min(listTime), 2)
slowest = round(max(listTime),2)
print('Fastest: ', fastest, 'seconds\nSlowest: ', slowest, 'seconds')
game = 1

print('\nList of Time:')
for i in range(len(listTime)):
    print('Game ', game, ' Time: ', listTime[i], ' Word: ', list_playerWords[i])
    game += 1
print()
if len(listMistakes) > 0:
    print('List of Mistakes')
    print('  The Word\tYour Input')
    for i in range(len(listMistakes)):
        print(i+1, ' ', listMistakes[i], ' : ', list_mistakenInput[i])

#this adds the new record to the existing list
record = name + ' ' + str(timeSum) + ' ' + str(fastest) + ' ' + str(slowest) + ' ' + str(score) + ' ' + str(10-score)

#this is where saving is done
write = open('TypingMaster - Records.txt', 'a')
print(record, file = write)
write.close()
os.system('pause')

#ARTEMIS - 04/04/20
