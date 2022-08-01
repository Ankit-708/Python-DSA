# inheriting the property of other class for making the code reusibility

class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"the name is {self.name}, salay is {self.salary}, and role is{self.role}"
    
    #class method

    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    # classmethod

    def from_desh(cls, string):
        return cls(*string.split("*"))

    #   static method

    def print_good(string):
        print("this is static method" + string)
        return 10

class Programmer(Employee):   # here it is inherit the property of employee class
    no_of_holiday = 56

    def __init__(self, aname, asalary, arole, language):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.language = language


    def printprog(self):
        return f"the programmers name is {self.name} and the salary is {self.salary} and the role is {self.role} and the languages are {self.language}"

ram = Employee("ankit", 233, "student")
shyam = Employee("rohan", 233, "employee")

shubham = Programmer("subham", 454, "progrmmer", ["python"])
karan = Programmer("karan", 656, "progrmmer", ["python"])

print(karan.printprog())

# print(karan.no_of_holiday)