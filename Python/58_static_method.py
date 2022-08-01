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

ram = Employee("ankit", 233, "student")
ram = Employee("rohan", 233, "employee")
shyam = Employee("mohan", 333, "painter")

# print(ram.no_of_leaves)

shyam.print_good("ankit")
print(shyam)