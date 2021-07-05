#Challenge No. 10

def intRoman(number):
        value = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        symbol = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        romanNum = ''
        i = 0
        while  number > 0:
            for j in range(number // value[i]): # this determines the loop by finiding which value is the number divisible to
                romanNum += symbol[i] # copies the symbol which the loop occured
                number -= value[i] # this decreases the number by the added in romanNum
            i += 1
        return romanNum
def roman(temp):
        if (temp == 'I'): 
                return 1
        if (temp == 'V'): 
                return 5
        if (temp == 'X'): 
                return 10
        if (temp == 'L'):
                return 50
        if (temp == 'C'): 
                return 100
        if (temp == 'D'): 
                return 500
        if (temp == 'M'): 
                return 1000
        return -1
def romanInt(string):
        number = 0
        i = 0
        while i < len(string):
                value1 = roman(string[i]) #this gets the first value
                if i+1 < len(string):#if by chance it is not 1 in length
                        value2 = roman(string[i+1])
                        if value1 >= value2:
                                number += value1 #this means that the first roman numeral is >= to the second
                                i += 1
                        else: #if the second roman character is greater than the first
                                number += (value2-value1)
                                i += 2
                else: 
                    number += value1 
                    i += 1
        return number

print('\nNumber to Roman Numeral Conversion')
print('\nChoose:\n[1]. Number to Roman Numeral\n[2]. Roman Numeral to Numbers')
choice = int(input('Enter Choice: '))
if choice == 1:
        value = int(input('\nEnter a Number: '))
        print('Roman Numeral: ', intRoman(value))
elif choice == 2:
        values = input('\nEnter a Roman Numeral: ')
        print('Number: ', romanInt(values))
#ARTEMIS - 04/02/20
