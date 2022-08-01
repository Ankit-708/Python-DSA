class Employee:
    no_of_leabes = 9

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole
    
    def printdetails(self):
        return f"the name is {self.name} an the salay is {self.salary} and the role is {self.role}"

    # class method
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves
    
    # def __add__(self, other):  # we use here bunder for adding the two object an there salary like int and int    __add__ is a special method and e called it bunder method and it is helping in operator overloading
    #     return self.salary + other.salary

    def __truediv__(self, other):  # we use here bunder for adding the two object an there salary like int and int    __add__ is a special method and e called it bunder method and it is helping in operator overloading
        return self.salary / other.salary

    def __repr__(self):
        # return f"the name is {self.name} an the salay is {self.salary} and the role is {self.role}"
        return f"Employee {'(self.name)', (self.salary), '(self.role)'}"   # it will print as it is
    
    def __str__(self):
        return f"the name is {self.name} an the salay is {self.salary} and the role is {self.role}"

emp1 = Employee("Ankit", 121, "Programmer")
# emp2 = Employee("Rohit", 190, "Gamer")

# print(emp1 / emp2)

# print(emp1) # it will print __str__ first and then print repr unitil and unless we will not call

print(repr(emp1))