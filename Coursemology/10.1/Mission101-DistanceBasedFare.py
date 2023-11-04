#Programming I
###########################
#      Mission 10.1       #
#   Distance Based Fare   #   
###########################
#Background
#==========
#Distance-Based Fares (DBF) is a fare payment scheme currently used across public buses and MRT/LRT trains in Singapore.
#Fares are charged based on the total distance travelled (regardless if it is on a bus or train).
#The distance-based fare calculation is available in the distance-based-fare.csv file provided.
#Based on the route details of bus service 174 (bus_174.csv), write a program to meet the following requirements:
#a) Calculate the distance travelled based on the boarding and alighting bus stop
#b) Calculate the payable fare
#Return the result of the above answers in a list of two items (e.g., [29.0,1.90])
#Important Notes
#===============
#1) Comment out ALL input prompts before submitting.
#2) You MUST use the following variables
#   board, alight, distance, fare
#board = input('Enter boarding busstop: ')
#alight = input('Enter alighting busstop: ')
#board CODING FROM HERE
#======================
#Create your function here
def calculate_fare(board,alight):
    
    fare_dictionary = {}
    
    file = open("distance-based-fare.csv")
    fare_list = file.read().split("\n")
    for x in range(len(fare_list)):
        fare_list[x] = fare_list[x].split(",")
        '''
        try:
            fare_dictionary[fare_list[x][0]] = fare_list[x][1]
        except:
            continue
        '''
    file.close()
    
    busstop_dictionary = {}
    
    file = open("bus_174.csv")
    busstop_list = file.read().split("\n")
    for y in range(len(busstop_list)):
        try:
            busstop_list[y] = busstop_list[y].split(",")
            busstop_dictionary[busstop_list[y][1]] = busstop_list[y]
        except:
            continue
    file.close()
    
    distance = 0
    fare = 0
    board = float(busstop_dictionary.get(board)[0])
    alight = float(busstop_dictionary.get(alight)[0])
    distance = alight - board
    
    for i in range(len(fare_list)):
        try:
            if float(fare_list[i][0]) >= distance and distance > float(fare_list[i - 1][0]):
                fare = float(fare_list[i][1])/100
        except:
            continue
    
    return [distance, fare]
    
#Statement to call the function and print the result
#Remove the statement when submitting in Coursemology 
#print(calculate_fare(board, alight))
#input 22009,10499 output [29.0, 1.9]
#input 28169,42059 output [9.2, 1.29]
#input 42089,10041 output [16.9, 1.61]