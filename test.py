bikes = int(input('Enter number if bikes(Below 10): '))
rides = int(input('Enter rides: '))

l = ['A','B','C','D','F','G','H','I','J','K']
for i in range(1,rides+1,1):
	c = l[i-1]
	l[i-1] = l[bikes-i-1]
	l[bikes-i-1] = c
	print(l[i-1])



