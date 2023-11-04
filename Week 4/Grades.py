#Yeo Jin Rong, S10258457C, grade calculator
#Input
marks = int(input("Enter your marks here: "))


#process
x = 50
grades = ["F", "D", "D+", "C", "C+", "B", "B+", "A", "A+"]
comment = ["See me.", " ", " ", " ", " ", " ", " ", "Well Done.", "Excellent"]
for i in range(9):
    if marks < x:
            print("Grades: {}".format (grades[i]))
            print("{}".format (comment[i]))
            break
    elif marks > 85:
        print("Grades: {}".format (grades[8]))
        print("{}".format (comment[8]))
        break
    else:
        x = x + 5
            
