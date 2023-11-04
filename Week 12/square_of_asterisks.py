def print_square(side):
    for i in range (side):
        for j in range (side):
            print("*", end = " ")
        print("")
side = int(input("Enter the numbers of characters for side of square: "))

print_square(side)
