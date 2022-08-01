import time
from functools import lru_cache

@lru_cache(maxsize=3) # here maxsize is how many cache we want to give it will cache only starting 3 value after it will run as asusual time or we cn increase the max value if we want that we need it again
def some_work(n):
    # some task taken n seconds
    time.sleep(n)   # here we just assume that there is any function that takes  sec to run or take n number of time to run at that time use use this function to make our program faster 
    return n

if __name__=='__main__':
    print("now running one work")
    some_work(3)    # it takes  seconds to print

    print("done")
    some_work(3)    # once again it run
    
    print("once again done")
    some_work(3)    # once again it run

    print("done")
    some_work(3)    # once again it run
    
    print("once again done")
    some_work(3)    # once again it run



# it is same as browser chache or we can say that in chache it stores the value once after it. it does not delay to print if we call them again 
# once we decleared after it we can call it many time without taking time