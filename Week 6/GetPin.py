#input
correctpin = "12345"
correctEntry = False
tries = 3

while not correctEntry and tries > 0:
    pin = input("Enter pin: ")

    if pin == correctpin:
        print("Correct pin entered: ")
        correctEntry = True
    else:
        tries -= 1

        if tries > 0:
            print("Invalid pin. Please try again")
            print(f"You have {tries} tries left.")
        else:
            print("Invalid pin. You have no more tries.")
            print("Your account is locked.")

print("The End")
    
#no data validation needed :(
