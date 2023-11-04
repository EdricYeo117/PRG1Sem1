# PRG03 Yeo Jin Rong, 25, S10258457, PRG Assignment 1

#imported modules
import urllib.request
import json

'''
Features:
1) Webscraping of API by data.gov.sg to obtain list of dictionaries for carpark availability
'''

def total_carpark():
    '''             ---- Option 1 ----
    Function to display total number of carparks
    This function uses len data_list to get total number of carparks
    '''                                                                                                                 
    total_carpark = len(data_list)
    #len() function used to get total elements in list of dictionaries
    print(f"Total Number of carparks in '{filepath}': {total_carpark}")


def total_basement_carpark():
    '''             ---- Option 2 ----
    Function to display all basement carparks
    Checks if basement carpark correlates with the value tied to key "Carpark Type
    '''
    basement_carpark_list = []
    print("{:<11} {:<23} {:<32}".format("Carpark No", "Carpark Type", "Address"))
    #makes a list of dict, by using filter() and lambda(), using an argument w/ lambda for parameter items
    basement_carpark_list = list(filter(lambda items: items["Carpark Type"] == "BASEMENT CAR PARK", data_list))

    '''             ---- Alternative Method ----
    for items in data_list:
        if "BASEMENT CAR PARK" == items["Carpark Type"]:
            basement_carpark_list.append(items) 2
    '''
    
    for items in basement_carpark_list:
            print("{:<11} {:<23} {:<32}".format(items["Carpark Number"],items["Carpark Type"], items["Address"]))      
    print(f"Total number: {len(basement_carpark_list)}")


def read_carpark_availability():
    '''             ---- Option 3 ----
    Function to read certain carpark availability.csv
    Obtains api response from data.gov.sg and translates its data into a dictionary with key value pairs:
    {'Carpark Number' : Value, 'Total Lots' : Value, 'Lots Availalable' : Value}
    '''    
    #while loop that reads the file, using 2nd line as keys, subsequent values as values

# API endpoint URL that provides the JSON data
    api_url = "https://api.data.gov.sg/v1/transport/carpark-availability"

    try:
        #open api
        with urllib.request.urlopen(api_url) as response:
            #check response
            if response.status == 200:
            
                #read json data
                api_response = response.read().decode('utf-8')
                
                #parse with json
                parsed_response = json.loads(api_response)
                
                #extract data
                carpark_data = parsed_response["items"][0]["carpark_data"]

                #making an actual usable list
                for entry in carpark_data:
                    carpark_number = entry['carpark_number']
                    total_lots = entry['carpark_info'][0]['total_lots']
                    lots_available = entry['carpark_info'][0]['lots_available']
                    
                    cleaned_entry = {'Carpark Number': carpark_number,'Total Lots': total_lots,'Lots Available': lots_available}
                    cp_availability.append(cleaned_entry)
                for item in cp_availability:
                    #converts numerical data in dictionary to integer
                    item['Total Lots'] = int(item['Total Lots'])
                    item['Lots Available'] = int(item['Lots Available'])
                
            else:
                print(f"API request failed with status code: {response.status}")

    except urllib.error.URLError as e:
        print(f"Error: {e}")
    return cp_availability

def total_carpark_availability():
    '''         ---- Option 4 ----
    Function to print total number of carparks
    Counts the total number of items in list
    '''
    #uses len() to get total elements in list of dictionaries
    total_carpark = len(cp_availability)
    if len(cp_availability) == 0:
        print("Error, read file using option 3 first")
    else:
        print(f"Total Number of Carparks in the File: {total_carpark}")

def carpark_with_lots():
    '''
    Function to print carparks without available lots, option 5
    Checks for items with lots available = 0, prints with for loop
    '''
    temp_list = []
    #makes a list of dict, by using filter() and lambda(), using an argument w/ lambda for parameter items
    temp_list = list(filter(lambda items:items['Lots Available'] == 0, cp_availability))

    #for loop to calculate
    '''     ----Alternative Method----
    for items in cp_availability:
        if items['Lots Available'] == 0:
            temp_list.append(items) 
    '''
    
    for items in temp_list:
        print(f"Carpark Number : {items['Carpark Number']}")
    print(f"Total Number: {len(temp_list)}")

def carpark_pcnt_lots():
    '''             ---- Option 6 ----
    Function to print carparks with at least x% available lots
    Continues if no lots availabe, then checks percentage higher than input
    '''
    #while loop to check for percent being a float value
    while 1:
        try:
            percent = float(input("Enter the percentage required: "))
            break
        except:
            print("Error")
            print("Please re-enter the percentage required")
            continue

    #filter() function with lambda parameters checking if key ['Lots Available'] != 0, and percentage available >= input, cp_availability as iterable
    filtered_list = list(filter(lambda items: items['Lots Available'] != 0 and 
                                 (items["Lots Available"] / items["Total Lots"]) * 100 >= percent, cp_availability))
    
    #for loop to check for percent value, validates if value for key "Lots Available" is not 0
    '''             ---- Alternative Method ----
    for items in cp_availability:
        if items['Lots Available'] == 0:
            continue
        else:
            percent_check = float((items["Lots Available"] / items["Total Lots"]) * 100)
        if percent_check >= percent: 
            temp_list.append(items)
    '''

    #printing data
    print("{:<11} {:<23} {:<32} {:<40}".format("Carpark No", "Total Lots", "Lots Available", "Percentage"))
    for item in filtered_list:
        percent_check = float((item["Lots Available"] / item["Total Lots"]) * 100)
        print("{:<11} {:<23} {:<32} {:<40.1f}".format(item["Carpark Number"],item["Total Lots"], item["Lots Available"], percent_check))      
    print(f"Total number: {len(filtered_list)}")



def carpark_pcnt_lots_address(): 
    '''             ---- Option 7 ----
    Function to print carpark info w/ address with at least x% available lots
    Prompts user input for percentage, creates a unified list of required data
    '''
    #while loop to verify input is a float value
    while 1:
        try:
            percent = float(input("Enter the percentage required: "))
            break
        except:
            print("Error")
            print("Please re-enter the percentage required")
            continue
        
    matching_address_list = []
    print("{:<11} {:<23} {:<32} {:<40} {:<50}".format("Carpark No", "Total Lots", "Lots Available", "Percentage", "Address"))

    #filter() function with lambda parameters checking if key ['Lots Available'] != 0, and percentage available >= input, cp_availability as iterable
    filtered_list = list(filter(lambda items: items['Lots Available'] != 0 and 
                                 (items["Lots Available"] / items["Total Lots"]) * 100 >= percent, cp_availability))
 
    #for loop to check for percent value, validates if value for key "Lots Available" is not 0, uses a temp_list as intermediate variable but lambda is faster
    '''             ---- Alternative Method ----
    for items in cp_availability:
        if items['Lots Available'] == 0:
            continue
        else:
            percent_check = float((items["Lots Available"] / items["Total Lots"]) * 100)
        if percent_check >= percent: 
            temp_list.append(items)
     '''

    #function to make a merged list of dictionaries, refer to function for more info
    make_address_list(filtered_list)

    #printing data using for loop
    for item in filtered_list:
        percent_check = float((item["Lots Available"] / item["Total Lots"]) * 100)
        print("{:<11} {:<23} {:<32} {:<40.1f} {:<50}".format(item["Carpark Number"],item["Total Lots"], item["Lots Available"], percent_check, item['Address']))     
    print(f"Total number: {len(filtered_list)}")

def carpark_location_check():
    '''    ---- Option 8 ----
    Function to print carparks at a given location, includes NIL
    Prompts input for location, creates a list of dictionaries of required information 
    '''
    #input for location checking, upper() to validate
    location = input("Enter the carpark location: ").upper()
    #checks if there is a proper input for location
    if location.isalnum():
        #print header
        print("{:<11} {:<23} {:<32} {:<40} {:<50}".format("Carpark No", "Total Lots", "Lots Available", "Percentage", "Address"))
        #sorts by address first, to ensure no data is missing
        sorted_list = list(filter(lambda item: location in item['Address'], data_list))

        #creates a new dictionary, with carpark number as key, lots available and total lots as value
        cp_availability_check = {item['Carpark Number']: item for item in cp_availability}

        #updates the dictionaries in sorted list with the corresponding information in cp_availability_check dictionary
        for entry in sorted_list:
            carpark_number = entry['Carpark Number']
            if carpark_number in cp_availability_check:
                entry.update(cp_availability_check[carpark_number])

        #checks dictionaries in list if "Total Lots" and "Lots Available" are present
        for item in sorted_list:
            if "Total Lots" not in item:
                item["Total Lots"] = "N/A"
            if "Lots Available" not in item:
                item["Lots Available"] = "N/A"   

        #printing data with percentage of lots available calculated
        for item in sorted_list:
            try:
                percent_check = float((item["Lots Available"] / item["Total Lots"]) * 100)
            except:
                percent_check = 0
            print("{:<11} {:<23} {:<32} {:<40.1f} {:<50}".format(item["Carpark Number"],item["Total Lots"], item["Lots Available"], percent_check, item['Address']))
        #validation for code to run
        if len(sorted_list) > 0:
            print(f"Total number of carparks in location: {len(sorted_list)}")
        else:
            print("Error no carparks found at location")
    else:
        print("Please key in a location")

def max_carpark (): 
    '''             ----  Option 9 ----
    Function to display the carpark with most parking lots
    Check list of dictionaries, check for maximum value of lots available 
    '''
    max_lots = 0
    max_cp_info = {}
    merge_list = []

    #merging cp_availability and data_list together, forming a list with all information
    for i in cp_availability:
        for j in data_list:
            if (i["Carpark Number"] == j["Carpark Number"]):
                merge_dict = {**i, **j}
                merge_list.append(merge_dict)

    #checks if address is available in list, if not provided, a empty string is introduced
    for item in merge_list:
        if "Address" not in item:
            item["Address"] = " "

    #max() function, from an iterable <merge_list> with a 'key' parameter of key=lambda item:item['Total Lots']
    #lambda is used to access each individual value for key['Total Lots'], the final ['Total Lots'] at the end is to retrive the value
    max_lots = max(merge_list, key=lambda item: item['Total Lots'])['Total Lots']

    #list() and filiter() function used in conjuction with lambda, to find the dictonary in merge_list with the value of max_lots for key ["Total Lots"]
    max_cp = list(filter(lambda x: x['Total Lots'] == max_lots, merge_list))
    max_cp_info = max_cp[0]

    '''         ---- Alternative Code ----
    for items in merge_list:
         if items['Total Lots'] == max_lots:
            max_cp_info.update(items)
    '''
    
    percent_check = float((max_cp_info["Lots Available"] / max_cp_info["Total Lots"]) * 100)
    max_cp_info['Percentage Available'] = round(percent_check, 1)

    #printining data using loop, for key, value in dictionary
    for key, value in max_cp_info.items():
        print(f"{key}: {value}")

def carpark_file():
    '''             ---- Option 10 ----
    Funnction to create an output file with carpark avaialbility and sort by lots available

    Makes a unfied list of all information required, sorts by lots available, writes to file
    '''
    count = 0
    #makes a unified list, with data from input .csv from option 3 and key["Address"] from carpark-info
    make_address_list(cp_availability)
    #sorts the list by ascending order for in ['Lots Available'] in iterable cp_availability, lambda gives every value in key "Lots Available"
    sorted_list = sorted(cp_availability, key=lambda item:item['Lots Available'])
    
    #joins string value for address if it contains multiple "," and adds quotation marks 
    for items in sorted_list:
        if ","  in items['Address']:
            items['Address'] = f'"{items["Address"]}"'

    # Writing data to the file 
    file_path = "carpark-availability-with-addresses.csv"
    key_names = sorted_list[0].keys()

    with open(file_path, 'w') as file:
        header = ','.join(key_names)
        file.write(header + '\n')

        for item in sorted_list:
            row = f"{item['Carpark Number']},{item['Total Lots']},{item['Lots Available']},{item['Address']}"
            file.write(row + '\n')
            count +=1
        file.close()
    print(f"Total number of lines written to file: {count + 1}")

def read_carpark_info(filepath):
    '''
    Function to read file intially
    Reads file, taking headers as keys, subsequent lines as values
    '''
    data_list = []
    try:
        with open(filepath, "r") as file:
            lines = file.readlines()
            #first line is used as header, converted to key for dictionary
            header = lines[0].strip().split(",")
            for line in lines[1:]:
                #subsequent lines used as values
                values = line.strip().split(",")
                while len(values) > 4:
                    #joins 
                    values[3] = ','.join(map(str, values[3:])).strip('"')
                    values = values[:4]                
                temp_dict = dict(zip(header, values))
                data_list.append(temp_dict)
    except FileNotFoundError:
        print("FileNotFoundError")
    return data_list

def make_address_list(list1):
    ''' 
    Function to make a new list, used in various options
    Combines information from two lists, checks if carpark number same
    '''
    ##redfines data_dict to use carpark number as a key, address as values
    data_dict = {item["Carpark Number"]: item["Address"] for item in data_list}

    #update dictionaries in list1 with matching addresses from data_dict
    for cp_info in list1:
        cp_no = cp_info.get("Carpark Number")
        if cp_no in data_dict:
            cp_info['Address'] = data_dict[cp_no]
    
    #checks if address exists in dictionary, if not present, adds NI
    for item in list1:
        if "Address" not in item:
            item["Address"] = "N\A"
    
#function to display menu, uses a nested list and a for loop to print menu
def display_menu():
    ''' 
    Function to display menu, starts with programme
    Menu for programme
    '''
    menu = [
        ["1", "Display Total Number of Carparks in 'carpark-information.csv'"],
        ["2", "Display All Basement Carparks in 'carpark-information.csv'"],
        ["3","Read Carpark Availability Data File"],
        ["4", "Print Total Number of Carparks in the File Read in [3]"],
        ["5", "Display Carparks Without Available Lots"],
        ["6", "Display Carparks With At Least x% Available Lots"],
        ["7", "Display Addresses of Carparks With At Least x% Available Lots"],
        ["8", "Display All Carparks at Given Location with Omits"],
        ["9", "Display Carpark with Max Lots Availble"],
        ["10", "Create an Output File with Carpark Availability with Addresses and Sort by Lots Available"],
        ["0", "Exit"]
    ]

    print("MENU\n====")
    for row in menu:
        options, description = row
        print(f"[{options}] {description}")

#Global Variables
filepath = "carpark-information.csv"
data_list = read_carpark_info(filepath)    
cp_availability = []  

#while loop to print menu, flag used to validate if option 3 is ran before subsequent options
flag = False
while 1:
        '''
        While loop to intiate programme
        Elif statements to check for options 0-10 
        '''
        display_menu()
        try:
            option = int(input("Enter your option: "))
            if option == 1:
                print("\nOption 1: Display Total Number of Carparks in 'carpark-information.csv'")
                total_carpark()
            elif option == 2:
                print("\nOption 2: Display All Basement Carparks in 'carpark-information.csv'")
                total_basement_carpark()
            elif option == 3:
                print("\nOption 3: Read Carpark Availability from data.gov.sg website")
                read_carpark_availability()
                flag = True
            elif option == 4:
                if flag == True:
                    print("\nOption 4: Print Total Number of Carparks in the File Read in [3]")
                    total_carpark_availability()
                else:
                    print("Please read file with option 3 first")
            elif option == 5:
                if flag == True:
                    print("\nOption 5: Display Carparks without Available Lots")
                    carpark_with_lots()
                else:
                    print("Please read file with option 3 first")
            elif option == 6:
                if flag == True:
                    print("\nOption 6: Display Carparks With At Least x% Available Lots")
                    carpark_pcnt_lots()
                else:
                    print("Please read file with option 3 first")
            elif option == 7:
                if flag == True:
                    print("\nOption 7: Display Addresses of Carparks With At Least x% Available Lots")
                    carpark_pcnt_lots_address()
                else:
                    print("Please read file with option 3 first")
            elif option == 8:
                if flag == True:
                    print("\nOption 8: Display All Carparks at Given Location with Omits")
                    carpark_location_check()
                else:
                    print("Please read file with option 3 first")
            elif option == 9:
                if flag == True:
                    print("\nOption 9: Display Carpark with the Most Carparking Lots")
                    max_carpark()
                else:
                    print("Please read file with option 3 first")
            elif option == 10:
                if flag == True:
                    print("\nOption 10: Create an Output File with Carpark Availability with Addresses and Sort by Lots Available")
                    carpark_file()
                else:
                    print("Please read file with option 3 first")
            elif option == 0:
                print("Programme Exited")
                break
        except TypeError and ValueError:
            print("Error")
