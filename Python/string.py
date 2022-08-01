        # type casting

# a = "ankit"
# var = type(a)
# print(var)
# print(a)

        # different type to print a string
e = "3"
e = int(e)
print(type(e))


# a = '''ankit
#         vishwakarma'''
# print(a)

        # string slicing

# name = "ankit"
# print(name[0]) 

# # or
# print(name[0:4])

        # strip for remove all extra spaces between the string

# name = "        ankit"
# print(name.strip())

        # to find the length of the string
# name = "vishwakarma"
# print(len(name))
# name = "laptop"
# print(len(name))

        # upper to convert all the string into lower

# name = "AnkiT"
# print(name.lower())

#         # lower to convert all the string into upper

# name = "ankit"
# print(name.upper())

        # replace any alphabet with the help of index value

# name = "vishwakama" 
# var = name.replace("a", "s")
# # print(name.replace("v", "a"))
# print(var)

        # temp or format is -- is replace with the new one that we will enter

# stri = "this is ankit"
# # name1 = "vishwakrm"
# # name2 = "golu"
# stri2 = "ghar"
# temp = "this is a {} and this is {}".format(stri,stri2)
# print(temp)

# # ------------------------------------------------------------------
# # stri = "this is ankit"
# name1 = "vishwakrm"
# name2 = "golu"
# # stri2 = "ghar"
# temp = "this is a {} and this is {}".format(stri,stri2)
# print(temp)


#         # or formate string ort f string ------------------
# name = "this"
# name1 = "golu"
# temp = f"this {name} and {name1}"
# print(temp)

# # python collecton----------------------------------------------
# # 1 list

# lst = [1,2,1,3,4]
# var = type(lst)
# print(var)

# # slicing

# lst = [2,3,1,2,5]
# var = lst[0:2]
# print(var)

# # append()

# lst = [1,4,1,5,1,5]
# var = lst[2]
# lst.append(1001)
# print(lst)

# insert() 

# lst = [1,4,1,5,1,5]
# # lst[2] = 45
# lst.insert(1, 100)
# print(lst)

# remove

# lst = [1,4,1,5,1,5]
# # lst[2] = 45
# # var = lst[2]
# lst.remove(5)
# # var = lst
# print(lst)

# pop 

# lst = [1,4,1,5,1,5]
# lst.pop()
# print(lst)

# del

# lst = [1,4,1,5,1,5]
# # del lst[3] it will delete through index value   
# del lst[3]   
# var = lst
# print(var)

# clear

# lst = [1,4,1,5,1,5]
# lst.clear()
# print(lst)

# ------------------      Tuple         ------------

# a = ["ram", "shyam", "mohan", "mohit"]
# var = type(a)
# print(var)

# a = ["ram", "shyam", "mohan", "mohit"]
# a[0] = "rohit"
# # var = a
# print(a)

# type casitng  

# a = ["ram", "shyam", "mohan", "mohit"]
# a = list(a)
# var = type(a)
# print(var)

# # set

# s = {1,2,1,2,4,15,8,9,4,5,1,5,5,5}
# print(s)

# add

# s = {1,2,1,2,4,15,8,9,4,5,1,5,5,5}
# s.add(12345)
# print(s)

# update

# s = {1,2,1,2,4,15,8,9,4,5,1,5,5,5}
# s.update([1,12,23,34,4,5,5])
# print(s)

# len

# s = {1,2,1,2,4,15,8,9,4,5,1,5,5,5}
# print(len(s))

# ---------       dictionary      --------------

# ankitdict = {
#         "name" : "ankit",
#         "class" : "5th",
#         "marks" : "44",
#         "subject" : "4"
# }
# # print(ankitdict)
# ankitdict["marks"] = 55
# print(ankitdict["marks"])
# # print(ankitdict)


# ankitdict = {
#         "name" : "ankit",
#         "class" : "5th",
#         "marks" : "44",
#         "subject" : "4"
# }
# # print(ankitdict)
# # ankitdict["marks"] = 55
# print(ankitdict["marks"])
# # print(ankitdict)

# --------------  conditional statements------------------

# age = input("Enter your age: ")
# age = int(age)
# if(age>18):
#         print("You can drive car")
# else:
#         print("you can drive cycle")



# age = input("Enter your age: ")
# age = int(age)
# if(age>18):
#         print("You can drive car")
# elif(age == 18):
#         print("You can drive bike")
# else:
#         print("you can drive cycle")


# ------------------Loops------------------------------------

# for

# a = [1,32,"ram"]
# for item in a:
#         print(item)

# try something new
# ankitdict = {
#         "name" : "ankit",
#         "class" : "5th",
#         "marks" : "44",
#         "subject" : "4"
# }
# for item in ankitdict:
#         print(ankitdict)

# while

# i = 0
# while(i<=10):
#         print(i)
#         i = i+1

# break statement

# i = 0
# while(i<10):
#         print(i)
#         if i == 5:
#                 break
#         i = i+1

# continue statement

# i = 0
# while(i<10):
#         i = i+1
#         if i == 5:
#                 continue
#         print(i)


# --------------  function        ----------------------

# def greet():
#         print("hello")
# # greet()
# greet()


# def sum(a, b):
#         c = a + b
#         return c
# d = sum(4,4)
# print(d)

# def sum(a, b):
#         c = a - b
#         return c
# d = sum(4,4)
# print(d)


# def sum(a, b):
#         c = a * b
#         return c
# d = sum(4,4)
# print(d)


# def sum(a, b):
#         c = a / b
#         return c
# d = sum(4,4)
# print(d)

# def sum(a, b):
#         c = a % b
#         return c
# d = sum(4,4)
# print(d)
