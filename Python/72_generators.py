"""
Iterable - in this we use __init__() OR __getitem()
Itrator - in this use __next__()
Itration - we get iteation by itator
"""

from typing import Generator


def gen(n):
    for i in range(n):
        yield i     # here Yield is a generotor it generate the value at run time it geneate on fly value

# for i in range(10):
#     print(i)

# g = gen(121212112)
# print(g)    #   output  <generator object gen at 0x000001C3FA414120>

# Generator is a iterator in which we can iterate it only once time

# g = gen(3)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())

a = "ankit"             # we has defined a iiterable here 
ier = iter(a)           # we has defined a iiterable here 
print(ier.__next__())   # we has defined a iiterable here 
print(ier.__next__())   # we has defined a iiterable here 

# for c in a:
#     print(c)