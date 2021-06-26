a = int(input('Enter the first number\t:'))
b = int(input('Enter the second number\t:'))
c = int(input('Enter the third number\t:'))

big = (a if (a>c) else c) if (a>b) else (b if (b>c) else c)
print('The greatest of the three numbers is '+str(big))