# we use this agument to calculate the time that which loop or anything takes how much time to execute

import time

# initial = time.time()

# k = 0
# while(k<5):
#     print("this is ankit")
#     time.sleep(1) # it will sleep for 2 sec after once execute an run again after 2 sec or for limited secondss we can stop the pogram
#     k+=1    # k = k+1 
# print("While loop run in", time.time() - initial,"seconds")  # we use here -initial for substracting the time between initial time to entered  
#                                                              #  time.time import

# initial2 = time.time()
# for i in range(5):
#     print("this is ankit")
# print("For loop run in", time.time() - initial2, "seconds") #   same as while loop


#  it will pint the local time 
time.localtime = time.asctime(time.localtime(time.time()))   # this all are in-built function we can use it many times
print(time.localtime)

