import random
lst = ["s", "p", "sea"]

chance = 5
total_chance = 0
computer_point = 0
your_point = 0
print("\n")
print("\t\t\t\t\t Stone Paper Seasor game\t\t\t\t\t")
print(f"s for stone\np for paper\nsea for seasor")

while total_chance< chance:
    input1 = input("Stone, Paper, Seasor: ")
    random1 = random.choice(lst)

    if input1 == random1:
        print("Tie selected same!\n")
    
    elif input1 == "s" and random1 == "p":
        computer_point = computer_point + 1
        print(f"computer guess {random1} and You guess {input1}\n")
        print("compute win 1 point\n")
        print(f"Computer point is{computer_point} an Your points is {your_point}")
    
    elif input1 == "s" and random1 == "sea":
        your_point = your_point + 1
        print(f"Computer guess {random1} and you guess {input1} \n")
        print("You win 1 point\n")
        print(f"Computer points is {computer_point} and Your points is {your_point}")
        
    elif input1 == "p" and random1 == "sea":
        computer_point = computer_point + 1
        print(f"computer guess {random1} and You guess {input1} \n")
        print("compute win 1 point\n")
        print(f"Computer point is{computer_point} an Your points is {your_point}")
    
    elif input1 == "p" and random1 == "s":
        your_point = your_point + 1
        print(f"Computer guess {random1} and you guess {input1}\n")
        print("You win 1 point\n")
        print(f"Computer points is {computer_point} and Your points is {your_point}")

    elif input1 == "sea" and random1 == "s":
        computer_point = computer_point + 1
        print(f"computer guess {random1} and You guess {input1}\n")
        print("compute win 1 point\n")
        print(f"Computer point is{computer_point} an Your points is {your_point}")
    
    elif input1 == "sea" and random1 == "p":
        your_point = your_point + 1
        print(f"Computer guess {random1} and you guess {input1}\n")
        print("You win 1 point\n")
        print(f"Computer points is {computer_point} and Your points is {your_point}")
 
    else:
        print("Wrong Input")
    total_chance = total_chance + 1
    print(f"{chance - total_chance} is left out of {chance}")

print("Game Over!")

if computer_point == your_point:
    print("Game Tie Both are Winner\n")

elif computer_point > your_point:
    print("COmputer Win the game\n")

else:
    print("You Win the game\n")

print(f"computer points is {computer_point} and Your points is {your_point}\n")
print("\t\t\t\t\tHave a good gay\t\t\t\t\t")