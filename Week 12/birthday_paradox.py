import random
bday_list = []
print("This program demonstrates the birthday paradox.")

while True:
    day = random.randint(1, 365)
    print(f"{day} was randomly generated")
        
    if day in bday_list:
         break
    print(f"Duplicate day! This took {len(bday_list)} tries.")
        
    bday_list += [day]
