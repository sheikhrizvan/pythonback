num1 = int(input('Enter number 1: '))
num2 = int(input('Enter number 2: '))
print(' a:add \n s:subtract \n m:multiply \n d:divide ')
print('Select operation: ')
a = input()
if(a == 'a' or a == 'A'):
	print('Addition is: ', num1+num2)
elif(a == 's'or a == 'S'):
	print('substraction is: ', num1-num2)
elif(a == 'm' or a == 'M'):
	print('Multiplication is: ', num1*num2)
elif(a == 'd' or a == 'D'):
	print('Division is: ', num1/num2)
else:
	print('No valid operation selected')