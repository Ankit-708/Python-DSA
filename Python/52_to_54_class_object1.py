# class student:     # this is class
#     pass

# ram = student()           #this is object we can use the template of class once we make it
# shyam = student()         #this is object we can use the template of class once we make it
# print(ram, shyam)       #this is object we can use the template of class once we make it

# --------------------------------------------------------------------------------------------

# class student:
#     pass
# ram = student()
# shyam = student()

# ram.name = "ankit"
# ram.std = 12
# ram.section = 1
# print(ram.name) #    here we can call any of them by there variable name

# # --------------------------------------------------

# class student:
#     pass
# ram = student()
# shyam = student()

# ram.name = "ankit"
# ram.std = 12
# ram.section = 1

# shyam.name = "mohit"
# shyam.std = 1
# shyam.section = 12

# print(shyam.name) # we can use object at any time and can print as many time or any number

# ----------------------------------------------------------


#               instance and class vaiable                  

  
class student:
    no_of_level = 9
    pass
ram = student()
shyam = student()

ram.name = "ankit"
ram.std = 12
ram.section = 1
print(student.no_of_level)
print(student.__dict__) #    by dict we can print a dictionary
student.no_of_level = 8
shyam.name = "mohit"
shyam.std = 1
shyam.section = 12
print(student.no_of_level)  

# note ---  we can not change in instance  we can cange it in only in class
