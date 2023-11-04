#Programming I
########################
#     Mission 6.1      #
#    Average Marks     #
########################
#Background
#==========
#You are required to display the following students' names and their
#respective marks. Calculate and print the average mark for these students
#   1) John - 100
#   2) Tom - 75
#   3) Jane - 80
#   4) Jim - 20
#   5) Mary - 50
#   6) Steve - 70
#   7) Anne - 95
#Important Notes
#===============
#You are required to use a while loop.
#You MUST use the following variables
#   - student_list
#   - mark_list
#   - average
#START CODING FROM HERE
#======================
#Calculate and return the average mark
def calculate_average(student_list, mark_list):
    i = 0
    while i < len(student_list):
        student = student_list [i]
        mark = mark_list[i]
        print( i + 1, ")", student, "-", mark)
        i += 1
    
    total_mark = sum(mark_list)
    average = total_mark / len(student_list)   
    return average #Do not remove this line
#Create the lists student_list and mark_list
student_list = ["John", "Tom", "Jane", "Jim", "Mary", "Steve", "Anne"]
mark_list = [100, 75, 80, 20, 50, 70, 95]
    
#Do not remove the next line that calls the function to find the average
average = calculate_average(student_list, mark_list)
#Modify to print the average with description
print("The average mark is: ", average)
#output 70
