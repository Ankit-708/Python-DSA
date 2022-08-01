# from math import pi
import random
lst = ["s", "w", "g"]

chance = 10
no_of_chance = 0
computer_points = 0
your_points = 0

print("\t\t\t\t Snake Water Gun\t\t\t")
print(f"s for snake\n w for water\n g for gun")

while no_of_chance < chance:
    input1= input("Snake, water, gun: ")
    random1 = random.choice(lst)

    if input1 == random1:
        print("Tie both 0 points to each other\n ")
    
    elif input1 == "s" and random1 == "g":
        computer_points = computer_points + 1
        print(f"your guess{input1} and computer guess is {random1}\n")
        print("computer Win 1 point\n")
        print(f"computer point is {computer_points} and you points is {your_points}\n")

    elif input1 == "s" and random1 == "w":
        your_points = your_points + 1
        print(f"your guess{input1} and computer guess is {random1}\n")
        print("You win your 1 point\n")
        print(f"computer points is {computer_points} and your points is {your_points}\n")

    elif input1 == "w" and random1 == "s":
        computer_points = computer_points + 1
        print(f"your guess{input1} and computer guess is {random1}\n")
        print("Computer Win 1 point\n")
        print(f"Computer points is {computer_points} and Your points is {your_points}\n")
    
    elif input1 == "w" and random1 == "g":
        your_points = your_points + 1
        print(f"You guess is {input1} and computer guess is {random1}\n")
        print("You Win your 1 point\n")
        print(f"computer points is {computer_points} and your points is {your_points}\n")

    elif input1 == "g" and random1 == "s":
        your_points = your_points + 1
        print(f"you guess{input1} and computer guess is {random1}\n")
        print("you win 1 point\n")
        print(f"computer point is {computer_points} and You points is {your_points}\n")
    
    elif input1 == "g" and random1 == "w":
        computer_points = computer_points + 1
        print(f"You guess {input1} and computer guess is{random1}\n")
        print("computer win 1 point\n")
        print(f"Computer points is {computer_points}  and your points is {your_points}")
    else:
        print("You have wrong input\n")

    no_of_chance = no_of_chance + 1
    print(f"{chance - no_of_chance} is left out of {chance}\n")

print("game over!")

if computer_points == your_points:
    print(" Game Tie")
elif computer_points > your_points:
    print("Computer Win")
else:
    print("You win")

print(f"Computer points is{computer_points} and You points is {your_points}\n")
print("Have a Good Day")



