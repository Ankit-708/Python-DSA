from typing import ClassVar


class A:
    classvar1 = "I am a class variablein class A"
    def __init__(self):
        self.var1 = "i am inside class A's Constructor"
        self.classvar1 = "instance var in class A"
        self.special = "special"

class B(A):
    def __init__(self):
        super().__init__()  # by the help of super keyword we can inherit the poperty of other instance
        self.var1 = "i am inside class B's Constructor"
        self.classvar1 = "instance var in class B"
    Classva2 = "i am in class B"
a = A()
b = B()
# print(b.classvar1)
print(b.special, b.var1, b.classvar1)


        