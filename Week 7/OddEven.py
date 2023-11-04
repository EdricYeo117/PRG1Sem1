#Input
numbers =[]
while True:
    num = int(input("Please enter a number (0 to end): "))
    if num == 0:
        break
    numbers.append(num)

odd_numbers = []
even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

odd_numbers.sort()
even_numbers.sort()
average = sum(numbers) / len(numbers)

print("Odd numbers:", odd_numbers)
print("Even numbers:", even_numbers)
print("Average =", average)
