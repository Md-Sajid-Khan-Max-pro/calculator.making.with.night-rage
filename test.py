number1 = input('enter a number:')
number2 = input('enter the other number:')
logo ='''
1. +
2. -
3. *
4. /
'''
print logo
chose = input ('chose sign:  ')
if chose == 1:
print number1+number2
elif chose == 2:
    print number1-number2
    elif chose == 3:
        print number1*number2
    elif chose == 4:
        print number1/number2
    else:
        print wrong input