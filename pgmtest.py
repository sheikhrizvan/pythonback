n=int(input('Enter how many?'))
l1 = list()
for i in range(1,n+1):
	l1.append(int(input('Enter a number: ')))
d = dict()
c = 0
for i in l1:
	l = len(d)
	for j in d:
		if(j == i):
			d[j] +=1
		else:
		d.update({j,1})

print(d)

	
 
 