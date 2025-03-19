firstNumber = int(input('enter with the first number: '))
secondNumber = int(input('enter with the second number: '))
thirdNumber = int(input('enter with the third number: '))



if firstNumber > secondNumber: #we knows that the first number is greater than second number.

    if firstNumber > thirdNumber:
        print('The firstNumber is the largest')
    else:
        print('The thirdNumber is the largest')

elif secondNumber > firstNumber:
   
    if secondNumber > thirdNumber:
       print('The secondNumber is the largest')    
    else:
       print('The thirdNumber is the largest')

else: 
    print('The thirdNumber is the largest')