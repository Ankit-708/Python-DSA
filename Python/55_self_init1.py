# class Employee:
#     no_of_level = 8

#     def printdetails(self):   #this is moethod, we can like this as many
#         return(f"this is {self.name} salary is {self.salary} and role is {self.role}")        #this is moethod, we can like this as many
    
# ram = Employee()
# shyam = Employee()

# ram.name = "rohit"
# ram.salary = 100
# ram.role = "cricketer"

# shyam.name = "mohit"
# shyam.salary = 50
# shyam.role = "footboller"

# print(ram.printdetails())
# print(shyam.printdetails())

class Employee:
    no_of_level = 8
    def __init__(self,aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole
#        |               |
    # isinstance       argument

        def printdetails(self):   #this is moethod, we can like this as many
                    return(f"this is {self.name} salary is {self.salary} and role is {self.role}")

ram = Employee("rohit",455,"cricketer")         # this is called constuctor 
print(ram.salary)