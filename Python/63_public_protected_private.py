class Employee:
    no_of_leaves = 8
    var = 8
    _protec = 9       # protected variable is use by program in limited an it is use by _ 
    __proctec = 9      # Protected is used by the sign of __ double under score

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

emp = Employee("mohan", 323, "Programmer")
# print(emp._protec)
print(emp._Employee__proctec) # we can not access it there name if we have to access it then we have to give the class name eg we use here _employee and then private