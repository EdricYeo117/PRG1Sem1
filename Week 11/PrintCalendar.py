
day_list = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
days_total = int(input("Enter number of days: "))
day_1st = input("When is the first day of the week: ")

line = []
date = []

start = day_list.index(day_1st)
line += start * " "

for i in range(1,days_total + 1):
    line += [i]
    if (i + start) % 7 == 0:
        date += [line]
        line = []
    if i == days_total:
        if len(line) < 7:
            line += " " * (7 - len(line))
        date += [line]

print(f"\n{day_list[0]:>4}{day_list[1]:>4}{day_list[2]:>4}{day_list[3]:>4}{day_list[4]:>4}{day_list[5]:>4}{day_list[6]:>4}")
        
for b in date:
    print(f"{b[0]:>4}{b[1]:>4}{b[2]:>4}{b[3]:>4}{b[4]:>4}{b[5]:>4}{b[6]:>4}")
