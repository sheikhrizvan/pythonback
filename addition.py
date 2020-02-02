class Addition:
	def __init__(self):
		self.a=0
		self.b=0
	def readInput(self):
		self.a = int(input())
		self.b = int(input())
	def result(self):
		c = self.a + self.b
		print(c)


obj = Addition()
obj.readInput()

