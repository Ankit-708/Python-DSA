# we use agrs when we have unlimited of people and want to show there name at that time we one decleare a function an then name *args and then 
# and then we give there name in this tuple and can execute

#  *args 

# def funargs(normal, *args):
#     print(normal)
#     for item in args:
#         print(item)

# har = ["ankit", "ghanshyam", "aiman", "geeta"]  #this is in tuple form
# normal = "we are"
# funargs(normal, *har)



# **kwargs
#  we use it when there is a fix word or letter is well come in every line at tht time write a once time ( like key and value form)
# and afte it we any add items in kw many times 

def funargs(normal, *args, **kwargs):  #we can change its name from kwargs to anything but ** is mandatory
    print(normal)
    for item in args:
        print(item)
    print("\n now i would like to introduce our some heroes")
    for key, Value in kwargs.item():
        print(f"(key) is a (Value)")

har = ["ankit", "rohan", "mohan", "rohit"]
normal = ("i am a normal argument and the students are: ")
kw = ("rohan":"monitor", "ankit":"student", "ghanshyam":"deputy") # search about it
# funargs(normal, *args, **kw)