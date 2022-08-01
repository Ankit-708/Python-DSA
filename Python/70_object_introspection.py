#  to check the details of object that from which class we are inherit it this is called object introspection

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

skillf = Employee("skill", "F")
# print(skillf.email)

print(type(skillf))  #  it show that from which class we are inherit it  or type show that what is the type of object
print(type("this is ankit"))  # it will print str as type

# print(id("this is ankit"))  # it will print the id of object there is unique id of every object

o = "this is ankit"
# print(dir(o))  # it will print all the method that i can use here in this object 

import inspect
print(inspect.getmembers(skillf))  # it will print all the memeber that is present in the skillf function like all the details of all the function