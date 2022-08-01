# ----------    map -------------------

# numbers = ["3", "4", "5"]
# we can use this but this is not efficient  way if we are using python ten there is inbuilt module with the help of that we can print in another way

# for i  in range(len(numbers)):
#     numbers[i] = int(numbers[i])

# numbers[2] = numbers[2]+1
# print(numbers[2])

# using of map function

# numbers = ["3", "4", "5"]
# numbers = list(map(int, numbers)) # here we cange this tuple into list and apply map function and change it into fom str to int

# numbers[2] = numbers[2]+1 #here we add at index value 1 incrase by one 
# print(numbers[2]) #printing that index value

#sqaring here with the help of map

# def sq(a):
#     return a*a

# num = [1,2,3,4,5,6,7,8]
# square = list(map(sq,num))
# print(square)


# with the use of lambda function
# #  as same as previous
# num = [1,2,8,4,5,6,8,7]
# square = list(map(lambda x:x*x,num))
# print(square)

# ------------------------------------------

# def square(a):
#     return a*a
#                 #here once it will print square and one it will print cube 
# def cube(a):
#     return a*a*a

# func = [square, cube]
# for i in range(5):
#     val = list(map(lambda x:x(i),func))
#     print(val)

# ------------------------------------------

#  ------------filter----------------------


#  it will print all number greate thn 5


# lst  = [1,2,3,4,5,6,7,8,9]
# def is_geater_5(num):
#     return num>5

# gr_than_5 = list(filter(is_geater_5, lst))
# print(gr_than_5)

# ------------------------------------------

# ---------------   Reduce----------------

#   it will add all number that is present in list1 
from functools import reduce

list1 = [1,2,4,5]
num = 0
for i in list1:
    num = num + i
print(num)

