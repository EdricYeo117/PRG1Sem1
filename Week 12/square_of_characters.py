def print_square(side, x):
    for i in range (side):
        for j in range (side):
            print(x, end = " ")
        print("")
side = int(input("Enter the numbers of characters for side of square: "))
x = input('Enter the character to use: ')
print_square(side, x)
