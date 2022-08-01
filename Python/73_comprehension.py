 # this is list comprehension


# ls = []
# for i in range(30):
#     if i%3==0:
#         ls.append(i)
    
# print(ls)


# this is the corect way to create a table or print it but we can print it in another way with the help of list compresion 

# list comprehension

# ls = [i for i in range(30) if i%3==0]
# print(ls)

#   dictinory comprehension

# dict1 = {i:f"item{i}" for i in range(10) if i%2==0}
# print(dict1)

# dict1 = {i:f"item{i}" for i in range(10)}
# dict2 = {value:key for key, value in dict1.items()}  # for reverse the dictinoay we use the value.key pair
# print(dict1, "\n", dict2)

#    set comprehenion

#    it will remove duplicates or that is already there 
# dresses = { dress for dress in ["desss1", "dress2", "desss1", "dress2", "desss1", "dress2", "desss1", "dress2"]}
# print(dresses)

# #    list comprehension

# dresses = [ dress for dress in ["desss1", "dress2", "desss1", "dress2", "desss1", "dress2", "desss1", "dress2"]]  # now it will print all that is present in the list
# print(dresses)
# print(type(dresses))      # from this we can find out its type

#    generators comprehension

evens = (i for i in range(10) if i%2==0)
# print(type(evens))
#   or
# print(evens.__next__())
# print(evens.__next__())
# print(evens.__next__())


# or

for item in evens:
    print(item)
