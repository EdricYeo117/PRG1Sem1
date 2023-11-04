mark_list = [['Mary', 90.5], ['Charles', 60.4], ['John', 70.5], ['Javier', 32.0], ['Luke', 46.7]]
def obtain_grades(grades):
     if grades > 84.5:
        return "A+"
     elif grades > 79.5:
        return "A"
     elif grades > 74.5:
        return "B+"
     elif grades > 69.5:
        return "B"
     elif grades > 64.5:
        return "C+"
     elif grades > 59.5:
        return "C"
     elif grades > 54.5:
        return "D+"
     elif grades > 49.5:
        return "D"
     else:
        return "F"

print("{:<16}{:<9}{:<5}".format("Student Name","mark","Grade"))
for student in mark_list:
    grade = obtain_grades(student[1])
    print("{:<16}{:<10}{:<4}".format(student[0],student[1],grade))
