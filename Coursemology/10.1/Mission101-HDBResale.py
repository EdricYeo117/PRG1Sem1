#Programming I
#########################
#      Mission 10.1     #
#   HDB Resale Prices   #   
#########################
#Background
#==========
#Tom is conducting some research into HDB resale prices as part of his part-time work for a real estate agency.
#Write a program to find out the following:
#
#a) The 2022 average price for the 4-room flat type (in 2 decimal places)
#b) The number of transactions above the average resale prices in part (a)
#c) The town with the highest resale price for the 5-room flat type in 2022
#
#Return the result of the three parts in a list of 3 items (e.g., [34535.35,20,'Hougang']
#Important Notes
#===============
#1) Comment out ALL input prompts before submitting.
#2) You MUST use the following variables
#   four_room_average, above_average, town_highest
#Set the filename
#Remove this statement when submitting in Coursemology
filename = "HDB-Resale-Price.csv"
#START CODING FROM HERE
#======================
#Create your function here
def ReadCSV(filename):
    file = open(filename)
    
    line = file.read()
    line = line.split("\n")
    for a in range(len(line)):
        line[a] = line[a].split(",")
   
    #Part a
    four_room_average = 0
    four_room_house = 0
    
    for b in range(len(line)):
        if line[b][0][:4] == '2022' and line[b][2][0:1] == '4':
            try:
                four_room_average += int(line[b][3])
                four_room_house += 1
            except:
                continue
    four_room_average /= four_room_house
    four_room_average = round(four_room_average,2)
    #Part b
    
    above_average = 0
    
    for c in range(len(line)):
        if line[c][0][:4] == '2022' and line[c][2][0:1] == '4':
            try:
                if int(line[c][3]) > four_room_average:
                    above_average += 1
            except:
                continue
    
    #Part c
    
    town_highest = [0,""]
    for d in range(len(line)):
        if line[d][0][:4] == '2022' and line[d][2][0:1] == '5':
            try:
                if int(line[d][3]) > town_highest[0]:
                    town_highest = [int(line[d][3]),line[d][1]]
            except:
                continue
    town_highest = town_highest[1]
    return [four_room_average, above_average, town_highest]
    
#Statements to call the function, save result in variable result and print out
#to double-check your result returned from function
#Remove these statements when submitting in Coursemology
result = ReadCSV(filename)
print(result)
#output [566969.47, 29, 'QUEENSTOWN']