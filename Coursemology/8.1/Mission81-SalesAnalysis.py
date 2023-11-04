
#######################
#    Mission 8.1      #
#    Sales Analysis   #
#######################
#Background
#==========
#Tom is given a file that contains monthly sales data for a company. Each
#line of the file represents a month and consists of the month name followed
#by the sales amount for each day of that month, separated by commas.
#As the company does not open every day, there may not be as many sales data
#as the number of days for the month.
#Tom would like you to help to write a Python program to find the total sales
#for each month.
#Important Notes
#===============
#1) Comment out ALL input prompts before submitting.
#START CODING FROM HERE
#======================
#Function that takes the name of the data file, finds the total sales for
#each month in the data file and returns it as a nested list.
#The nested list should contain 12 elements, where each element is a list
#with month name and total sales for the month
def calculate_sales(filename):
    read = open(filename,"r")
    results = []
    loop = True
    while loop:
        file = read.readline()
        if file == "":
            loop = False
            break
        file = file.split(",")
        total = 0
        month = []
        for i in range(len(file)):
            if i == 0:
                month += [file[i]]
                continue
            total += int(file[i])
        month += [total]
        results += [month]
    
    # Add your code here...
    
    return results #do not remove this line
                       
#Prompt user for name of data file
#filename = input('Please enter the name of the data file: ')
    
#Do not remove the next line that calls the function
results = calculate_sales(filename)
#Modify to print the result as shown in the question in Coursemology
print()