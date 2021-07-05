import time
import random
import sys
import os


def logo():
    print('\t\t\t*************************************')
    print('\t\t\t*  Primrose Webster\'s Dictionary    *')
    print('\t\t\t*                Artemis 2020       *')
    print('\t\t\t*************************************')
start = time.time()
#original text
listText = [line.strip().lower() for line in open('Dictionary.txt')]

#definition of listword, meaning and the final dictionary
listWord = ['']*(len(listText)//2)# '' times the length of listText divided by 2 
listMeaning = ['']*(len(listText)//2)# bc the lisrText has the length of words and Meaning
finalDictionary = {}

#getting the values of word and meaning from text
j = 0
for i in range(len(listText)): #this is for the words
    if i % 2 == 0: # here it extracts all the words in the listText
        listWord[j] = listText[i] # into the listWord using a loop
        j += 1
j = 0
for i in range(len(listText)):# this is for the meanings
    if i % 2 != 0:
        listMeaning[j] = listText[i]
        j += 1
end = time.time()
#transfering all words and meaning to dictionary
for i in range(len(listWord)):#it transfers the words into the finalDictionary
    finalDictionary[listWord[i]] = listMeaning[i] #ex. [word[i], meaning[i]] for every word there is a meaning

while True:
    os.system('cls')
    logo()
    print('\nDatabase loaded', len(listWord), 'words in', round((end-start),2), 'seconds', sep = ' ')
    rand = random.randrange(0, len(listWord))
    print('\nWord of the Day:', listWord[rand].upper(), '\n- ', listMeaning[rand])

    print('\nChoose:\n[1]. Search Word\n[2]. Add new Word')
    choice = int(input('Enter choice: '))
    if choice == 2:
        os.system('cls')
        logo()
        access = input('\n\nEnter Password: ')
        password = 'primrose'
        if access == password: # predefined password
            word = input('\nEnter New Word: ')
            meaning = input('Enter Meaning: ')
            if word.lower() in listWord:
                print('Invalid Word! It already exist!')
                os.system('pause')
                continue
            else:
                write = open('Dictionary.txt', 'a')
                print(word, file = write)
                print(meaning, file = write)
                write.close()
                print('\n', word, 'is now added!')
                os.system('pause')
                sys.exit()
        else:
            print('Invalid Password! Please Try again.')
            os.system('pause')
            continue
    elif choice > 2 or choice < 1:
        print('Invalid Input! Please Try again!')
        os.system('pause')
        continue
    else:
        break
lower = ''
counter = 0
found = 0
while found == 0:
    os.system('cls')
    logo()
    print('\nDatabase loaded', len(listWord), 'words in', round((end-start),2), 'seconds', sep = ' ')
    search = input('\nEnter word: ')
    lower = search.lower() #this is used to index other possible words
    for key, value in finalDictionary.items():#this is where the searching done
        if search.lower() == key.lower():
            print('\n[Word Found!]')
            print('  ', key.upper(), '\n-', value)

            print('\nOther Possible Words: ')
            for word, value in finalDictionary.items():#this is where it finds other possible words
                if lower in word:
                    print(' ', word.upper())
                    counter += 1
                if counter == 5:
                    break
            found = 1
    if found == 0:
        print('\t[Word not Found!]')
        print('\nOther Possible Words: ')
        for word, value in finalDictionary.items():
                if lower in word:
                    print(' ', word.upper())
                    counter += 1
                if counter == 5:
                    break
    print('\nWould you like to search again?\n[1]. Yes\n[2]. No')
    found = 0
    choice = int(input('\nEnter Choice: '))
    if choice == 1:
        continue
    if choice >= 2:
        break
sys.exit()


#ARTEMIS - 04/02/20

