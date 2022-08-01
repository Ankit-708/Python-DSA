class Libray:
    def __init__(self, list, name):     #here we have made a constructor after it   
        self.booklist = list            #here we have made a constructor after it 
        self.name = name            #here we have made a constructor after it 
        self.lenddict = {}          #here we have made a constructor after it 
    
    def displaybook(self):
        print(f"We have following books in ou library: {self.name}")
        for book in self.booklist:
            print(book)
    
    def lenbook(self, user, book):
        if book not in self.lenddict.keys():
            self.lenddict.update({book:user})
            print("Lender-Book batabase has been updated. You can take book now")
        else:
            print(f"Book is already being used by {self.lenddict[book]}")

    def addbook(self, book):
        self.booklist.append(book)
        print("Book hs been added to the book list")

    def returnbook(self, book):
        self.lenddict.pop(book)

if __name__ == '__main__':
    oxford = Libray(['Python', 'TOC', 'DBMS', 'IWT'], "ankitvish")

    while(True):
        print(f"welcome to the {oxford.name} library. Enter your choice to continue")
        print("1. Display Books")
        print("2. Lend a Books")
        print("3. Add a Books")
        print("4. Return a Books")

        user_choice = int(input())

        if user_choice == 1:
            oxford.displaybook()

        elif user_choice == 2:
            book = input("Enter the name of the book you want to lend: ")    
            user = input("Enter your name: ")
            oxford.lenbook(user, book)

        elif user_choice == 3:
            book = input("Ente the name of the book yo want to add: ")    
            oxford.addbook(book)

        elif user_choice == 4:
            book = input("Enter the name of the book you want to return: ")
            oxford.returnbook(book)

        else:
            print("Not a valid option")    

        print("Press q to quit and c to continue")
        user_choice2 = ""
        while(user_choice2!="c" and user_choice2!="q"):
            user_choice2 = input()
            if user_choice2 == "q":
                exit()

            if user_choice2 == "c":
                continue



