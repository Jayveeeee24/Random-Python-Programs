#Challenge No.2
#Currency Denomination

currency = [1000, 500, 200, 100, 50,20,10,5,1]

print('Currency Denomination')
value = float(input('Enter a Number: '))

intValue = int(value)
decimalValue = (value - intValue)/25*100
i = 0
while intValue > 0:
    print('PHP ', currency[i], ' : ', intValue//currency[i])
    intValue = intValue % currency[i] #this gets the remainder value from dividing the value with the currency
    i += 1
print('25 cents : ', int(decimalValue))

import os
os.system("pause")
#ARTEMIS - 03/28/20
