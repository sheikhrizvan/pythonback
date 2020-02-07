#Organize Later
# Variable Declaration
class Employee:
    def __init__(self):
        self.empid = input("Enter Employee ID: ") #auto generate later
        self.empfname = input("Enter First Name: ")
        self.emplname = input("Enter Last Name: ")
        self.emptech = input("Enter Technology: ")
        self.empdsg = input("Enter Designation: ")
        self.empsal = int(input("Enter Salary: "))
        self.empjdt = input("Enter Joining date: ")
        self.empstatus = 'Active'

    def displayEmpData(self):
        '''print ('Emp Id is: %'.format(self.empid)
        print ("Emp First Name is: ", self.empfname)
        print ('Emp Last Name is: %'.format(self.emplname)
        print ('Emp Designation is: %'.format(self.empdsg)
        print ('Emp Technology is: %'.format(self.emptech)
        print ('Emp Joining Date is: %'.format(self.empjdt)
        print ('Emp Salary is: %'.format(self.empsal)
        print ('Emp Status is: %'.format(self.empstatus)'''
        try:
            empfile=Open(self.empid, 'wa')
            empfile.write(self.empid+'\n'+self.empfname+self.emplname+'\n')
            empfile.append(self.empjdt+'\n'+self.emptech+'\n'+self.emptech+'\n'+self.empdsg+'\n'+self.empsal+'\n')
            empfile.append(self.empstatus)
        except FileExistsError:
            print('Error occured in file...')


obj = Employee()
obj.displayEmpData()