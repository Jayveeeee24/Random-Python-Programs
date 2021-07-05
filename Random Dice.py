#Challenge No.6
'''
This program determines the probability of a random thrown dice within its random size
'''
import random
import os
'''
LEGEND
    List1 -- contains the sum of dice thrown
    List2 -- contains how many outcomes does the random have
    (ex. the random list has 25 outcomes of 2)
    tempList -- contains the basis for probability (sums of each dice)
    listFinal -- contains the percentage of outcomes
''' 

List1 = []
for i in range(random.randrange(1, 10000)):
    rand1 = random.randrange(1, 7) # dice 1
    rand2 = random.randrange(1, 7) # dice 2
    List1.append(rand1+rand2) # it gives the sum of each dice to the list
    
tempList = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
List2 = [0]*11
for i in range(len(List1)):     # here it iterates through the List1 
        for j in range(len(tempList)):# if it contains number in temp
            if List1[i] == tempList[j]: # it iterates the counter which is List2
                List2[j] = List2[j] + 1 

print('\nTotal Number of Items: ', len(List1))
print('List of Outcome:')


listFinal = []
for i in range(len(List2)):
    listFinal.append(round(List2[i]/len(List1), 2))

totalPercent = sum(listFinal)
for i in range(len(List2)): # this prints temp and its outcome and percentage
    listFinal[i] = str(listFinal[i]).lstrip('0')
    listFinal[i] = str(listFinal[i]).lstrip('.')
    final = str(listFinal[i]).lstrip('0')
    print(tempList[i], ': ', List2[i], ' : ', final, '%')


os.system("pause")
                     
# ARTEMIS - 03/30/20
