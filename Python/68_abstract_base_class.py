from abc import ABCMeta, abstractclassmethod

class Shape(metaclass = ABCMeta):
    @abstractclassmethod
    def printarea(self):
        return 0

class Rectangle(Shape):
    type = "Rectangle"
    side = 4
    def __init__(self):
        self.length = 6
        self.breadth = 7

    def printarea(self):
        return self.length * self.breadth

rect1 = Rectangle()

# abc is  module abc is a meta class  we can inherit any class by the help of meta class 
# if we are inherit anything from class abcmeta 