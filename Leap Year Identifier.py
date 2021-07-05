#Challenge No. 4
import sys

print('\nLeap Year Identifier')
val = int(input('Enter Year(1600+): '))
if val < 1600:
    print('Invalid Input!')
else:
    if (val%4 == 0 or val%400 == 0) and not val%100 == 0:
        print('The Year: ', val, ' is a Leap Year!')
    else:
        print('The Year: ', val, ' is not a Leap Year')

print('\nLeap Year Counter')
counter = 0
for i in range(1600, val, 4):
    if i%100 == 0 and not(i%400 == 0):
        continue
    counter += 1
print('There are ', counter, ' leap years between 1600 and ', val)

print('\nDo you want to print all the leap years?\nChoose:\n[1]. Yes\n[2]. No')
choice = int(input('Enter Choice: '))


if choice == 1:
    print('\nThese are all the leap years between ', 1600, '-', val)
    for i in range(1600, val, 4):
        if i%100 == 0 and not(i%400 == 0):
            continue
        print(i, end = ' ')
elif choice == 2:
    sys.exit()
else:
    print('\nInvalid Input! System will exit')
    sys.exit()

#ARTEMIS - 03/29/20
