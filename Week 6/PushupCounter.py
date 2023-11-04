#Input

target = int(input("Enter target number of pushups: "))


#process
total = 0
days = 0

while total < target:
    days += 1
    pushups = int(input("Day {}: How many pushups did you do today?".format(days)))
    total += pushups


print(f"You did a total of {total} pushups.")
print(f"You hit your target in {days} days!")
