# principal = float(input("Enter the pricipal amount: "))
# time = float(input("enter the time duration: "))
# rate = float(input("enter the rate: "))
# sum = (principal*rate*time)/100
# print(sum)

def prime(num):
    flag = False
    if num>1:
        for i in range (2, num):
            if (num % 2 == 0):
                flag = True
            break
    if flag:
        print("not prime number")
    else:
        print("prime number")

    a = int(input("enter the number: "))
    print(a)
# prime(num)

