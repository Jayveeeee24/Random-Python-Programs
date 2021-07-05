#Challenge No. 3
import math

print('Time Converter')

choice = int(input('[1]. Seconds to Time\n[2]. Minutes to Time\nChoose: '))
if choice == 1:
    value = int(input('\nInput Seconds: '))
    
    hrs = value//3600 #1hr is equal to 3600 secs
    mins = (value%3600)//60 # the remainder from hr is divided to 60 which is minutes
    sec = ((value%3600)%60) # the remainder of min from the remainder of hr is seconds

    if hrs >= 1:
        print('Time: {:,d}hr. '.format(hrs) , mins, 'min. ', sec, 'secs.')
    else:
        mins = value//60
        sec = value%60
        print('Time: {:,d}min. '.format(mins), sec, 'secs.')
        
if choice == 2:
    value = int(input('\nInput Minutes: '))

    hrs = value//60 # the value entered is divided by 60 to get hr
    mins = (value % 60) # the remainder from of divided value to hr is the minutes

    if hrs >= 1:
        print('Time: {:,d}hr. '.format(hrs), mins, 'min. ')
    else:
        mins = value
        print('Time: {:,d}min. '.format(mins), ' or')
        print('Time: Seconds: {:,d}'.format(value * 60))

                

#ARTEMIS - 03/28/20
