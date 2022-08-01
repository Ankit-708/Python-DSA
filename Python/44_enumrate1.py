l1 = ["aalo", "gazar", "bhindi", "pizza", "burger"]

# i = 1
# for item in l1:
#     if i%2 != 0:
#         print(f"pls give me {item}")
#         i = i+1

#   this enumrate function once we call it from list then and decleaed with the help of conditionl statement after it we call it one by one  
#   as we can see here 

# print(type(l1))

for index, item in enumerate(l1):
    if index%2==0:
        print(f"please give me {item}") 