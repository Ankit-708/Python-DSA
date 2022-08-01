from genericpath import exists
import os
# ------  cwd -------------
# print(dir(os))
# print(os.getcwd())  # this print current working directory or it will print the current directiory

# os.chdir("c://") # this is used to change the current directiory 
# print(os.getcwd())

#-------------------- list dir

# print(os.listdir())  #  it will print all the files that is present in the current directiory or we can also check another file details also

# print(os.listdir("c://"))  #  it will print all the files that is presnt in the c directiory
# print(type(os.listdir("c://")))  #or we can check its type

#  for making a folder we use---------------

# os.mkdir("this") # we can make  folder by this name
#  # or if we want that there should be anothe folder in this folder then we use

# os.makedirs("this/that")  # this will create an another folder in this folder

# ------- rename

# or we can rename the file or foler tht is persent in the curent directiory fo this we have to use

# os.name("ankit.txt", "ankitvishwakrma.txt") # first old file name and after new file name

# ----------- Environment variable

# we can see that what is the environment vaiable in our system by using this commands o any other environment like path or home etc that what ever we want

# print(os.environ.get('Path'))  # by using this code we can find out what are the paths that is present in our system

# -------join function
# it is join two path with accuracy or in this function there is no headtch of / forword slace we can use  it

# print(os.path.join("c:/", "ankit.txt"))   # two different file location we are joining here

# ---------------exists

# this function tell us that the path ius existing or not in our our system it will check and retun in boolen form like true o false


print(os.path.exists("c://")) # it will print true if file is exits or false if file is not exists it is used for directiory

# ----------------- for file directiory

# print(os.path.isfile("c://progam files"))  # if this file is present in the diectiory then it will print true otherwise it will print false 






