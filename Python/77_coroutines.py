#   actually we use corooutines beacuse if we want that there is some line of code that will run after and after from the middle of the code only that portion will run at that time we use  
from typing import Text

#   first this one will run 

def searcher():
    import time
    # some 4 seconds time consuming task
    book = "this is a python tutoial"
    time.sleep(4)

# after it it will run contineusily that's what here have used while loop 

    while True:
        text = (yield)  # it will geneate the value on the fly
        if text in book:
            print("you text is in the book")
        else:
            print("text is not in the book")
        
search = searcher()
next(search) # it is calling only once time after this it is executing from the yield 

search.send("ankit")

# or we can close coroutine 
search.close()


input("Press any key")

search.send("ankit vishwakarma")