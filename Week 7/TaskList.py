days = int(input("Enter number of days: "))
print("Day | Task(s)")
print("----|---------")

for day in range(1, days + 1):
    if (day - 1) % 7 == 0:
           print("Day | Task(s)")
           print("----|---------")
    print("{:3} |  ".format(day))
          
