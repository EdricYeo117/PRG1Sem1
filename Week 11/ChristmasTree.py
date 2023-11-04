character = input("Enter a character: ")
number = int(input("Enter a number: "))

for i in range(number):
    line = (number - 1 - i) * " " + (character + " ") * (i + 1)
    print(line)

print("Merry Christmas!")
*