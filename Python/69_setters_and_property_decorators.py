class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname} {lname} @gmail.com"

    def explain(self):
        return f"The {self.fname} and {self.lname}"
    
    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return "email is not found pls set it using setter"
        return f"{self.fname} {self.lname} @gmail.com"

    @email.setter   #   decorator
    def email(self, string):
        print("setting now...")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

ram = Employee("ram", "seeta")
shayam = Employee("shayam", "mohan")

# print(ram.explain())
# print(ram.email)

# print(ram.email())

# after using @property o we can say that after using decoratos  
print(ram.email)
ram.fname = "raj_ji"
# print(ram.email())

print(ram.email)

ram.email = "this.that@gmail.com"
print(ram.email)  # here we can check anything that what is name and other things

del ram.email
print(ram.email) # now it will not print it will print none 