# def function1():
#     print("This")

# func2 = function1
# del function1
# print(func2)

# def funcret(num):
#     if num == 0:
#         return print
#     if num == 1:
#         return sum 
# a = funcret(1)  #   what ever we will type at place of 1 that function will call and execute that part 
# print(a)

# # ----------------------------------------------------------------

# def executor(func):
#     func("this")

# executor(print)
#  it will print as it is 
# -------------------------------------------------------------------

def dec1(func1):
    def nowexec():
        print("Executing now")
        func1()
        print("Executed")
    return nowexec

#dec1
def who_is():
    print("this is a ")

who_is = dec1(who_is)
who_is()   #    "this is" function will print the statement in the middle like a sandwich it depend where we call

