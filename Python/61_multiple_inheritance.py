# deived by two or more class is called multiple inheritance

class Employee:
    no_of_leaves = 8
    var = 8

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

class Player:
    var = 9
    no_of_game = 4
    def __init__(self, name, game):
        self.name = name
        self.game = game
    
    def printdetails(self):
        return f"The name is {self.name} and the game is {self.game}"
        
class CoolProgramme(Employee, Player):   # it depend on order means what we call first  
    var = 10
    language = "python"
    def printlanguages(self):
        print(self.language)


ram = Employee("ankit", 233, "student")
shyam = Employee("rohan", 233, "employee")

shubham = Player("Shubham", ["cricket"])
karan = CoolProgramme("Karan", 333, "coolpogrammer")
# det = karan.printdetails()
# karan.printlanguages()

# print(det)

print(karan.var)

