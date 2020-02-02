class Person:
	def __init__(self, fn, ln):
		self.fname = fn
		self.lname = ln
	def display(self):
		print('Name is ', self.fname, ' ', self.lname)

class Student(Person):
	def __init__(self, fn, ln, rno):
		super().__init__(fn,ln)
		self.rollno = rno
	def display(self):
		super().display()
		print('Roll No is: ', self.rollno)

fname = input('Enter First name: ')
lname = input('Enter Last name: ')
rno = int(input('Enter roll number: '))
obj = Student(fname, lname, rno)
obj.display()
p = Person('ccccc', 'dddddd')
p.display()
