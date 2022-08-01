f1 = open("ankit.txt")

try:
    f = open("does.txt")

except Exception as e:
    print(e)
 
# this will run only if except is not ruunning

else:
    print("this will run only if except is not ruunning")

finally:  # we use finally because we want to run this program anyway either the file is exist or not program should run this
    print("run anyway")    # or for code clean up
    f1.close()

print("importanty stuff")