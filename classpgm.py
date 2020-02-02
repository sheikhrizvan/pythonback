class person:
	def __init__(self,name,age):
		self.name = name
		self.age = age
	def dsp(self):
		print('Name is: ', self.name)
		print('Age is: ', self.age)
	def updatevalue(self, nm, ag):
		
		self.name = nm
		
		self.age = ag

p1 = person("aaaaaaaa",30)
print(p1.name)
print(p1.age)
p1.dsp()
p1.updatevalue('bbbbbbb',1)
p1.dsp()

