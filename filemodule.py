def readData(fname):
	myfile = open(fname, 'r')
	print(myfile.read())

def writeData(fname, data):
	myfile = open(fname, 'w')
	myfile.Write(data)


nm = 'testfiles//' + input('Enter file name: ')
data = input('Enter file data: ')
writeData(nm, data)
readData(nm)
