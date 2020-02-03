a = int(input('Enter number 1:'))
b = int(input('Enter number 2:'))
print('Addition: ',a+b)
print('Substraction: ',a-b)
print('Multiplication: ',a*b)
try:
	print('Division: ',a//b)

except:
	print('Denominator > 0')  
else:
	print('This is just like finally exception block in java')