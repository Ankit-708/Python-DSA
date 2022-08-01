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

        #   class method
        def change_leaves(cls, newleaves):  #    we can access class method by instance and class and modify acccordingy
            cls.no_of_leaves = newleaves      #  we can access class method by instance and class and modify acccordingy

ram = Employee("rohit",455,"cricketer")         # this is called constuctor 
ram = Employee("mohit",555,"basketball")         # this is called constuctor 

ram.change_leaves(12)

print(ram.no_of_leaves)