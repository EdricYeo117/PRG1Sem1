# PRG03 Yeo Jin Rong, 25, S10258457, PRG Assignment 1

'''
Features:
1) GUI Display Menu, with additional prompts for input (Options 6,7,8,9) and file selection (Options 3)
'''

def total_carpark():
    '''             ---- Option 1 ----
    Function to display total number of carparks
    This function uses len data_list to get total number of carparks
    '''                                                                                                                                               
    total_carpark = len(data_list)
    #len() function used to get total elements in list of dictionaries
    print(f"Total Number of carparks in '{filepath}': {total_carpark}")

    result = "Option 1 Selected: Displayed Total Number of Carparks"
    display_result(result)

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
    result = "Option 2 Selected: Displayed All Basement Carparks"
    display_result(result)

def read_carpark_availability(filepath):
    '''             ---- Option 3 ----
    Function to read certain carpark availability.csv
    Uses while loop, first line as header, subsequent line as data
    checks if value is digit, converts to integer
    '''    
    #while loop that reads the file, using 2nd line as keys, subsequent values as values
    while 1:
        try:
            with open(filepath, "r") as file:
                lines = file.readlines()
                #2nd line of file marked as header, used as key for dictionary
                header = lines[1].strip().split(",")
                #1st line of file marked as timestamp, to be printed
                timestamp = lines[0]

                for line in lines[2:]:
                    #3rd line onwards marked as values
                    values = line.strip().split(",")
                    #uses zip() to combine key=header, values=value, into a dictionary
                    temp_dict = dict(zip(header, values))
                    cp_availability.append(temp_dict)

                for item in cp_availability:
                    #converts numerical data in dictionary to integer
                    item['Total Lots'] = int(item['Total Lots'])
                    item['Lots Available'] = int(item['Lots Available'])
                
                print(f"Timestamp:{timestamp}")
                file.close()
            break
        except FileNotFoundError:
            print("Error please select file again")
            break

def total_carpark_availability():
    '''         ---- Option 4 ----
    Function to print total number of carparks
    Counts the total number of items in list
    '''    
    #uses len() to get total elements in list of dictionaries
    total_carpark = len(cp_availability)
    if len(cp_availability) == 0:
        print("\nError, read file using option 3 first")
    else:
        print(f"\nTotal Number of Carparks in the File: {total_carpark}")
    result = "Option 4 Selected: Displayed Total Carpark Avaialbility"
    display_result(result)   

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
    result = "Option 5 Selected: Displayed Carparks without Lots Available"
    display_result(result)

def carpark_pcnt_lots(percent):
    '''             ---- Option 6 ----
    Function to print carparks with at least x% available lots
    Continues if no lots availabe, then checks percentage higher than input
    '''
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
    #Printing data from list
    print("{:<11} {:<23} {:<32} {:<40}".format("Carpark No", "Total Lots", "Lots Available", "Percentage"))
    for item in filtered_list:
        percent_check = float((item["Lots Available"] / item["Total Lots"]) * 100)
        print("{:<11} {:<23} {:<32} {:<40.1f}".format(item["Carpark Number"],item["Total Lots"], item["Lots Available"], percent_check))      
    print(f"Total number: {len(filtered_list)}")
    result = "Option 6 Selected: Displayed Carparks available by Percentage"
    display_result(result)

def carpark_pcnt_lots_address(percent): 
    '''             ---- Option 7 ----
    Function to print carpark info w/ address with at least x% available lots
    Prompts user input for percentage, creates a unified list of required data
    '''
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
    result = "Option 7 Selected: Displayed Carparks available by Percentage with Address"
    display_result(result)

def carpark_location_check(location):
    '''                 ---- Option 8 ----
    Function to print carparks at a given location, including N/A
    Prompts input for location, creates a list of dictionaries of required information 
    '''
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
    result = "Option 8 Selected: Displayed Carparks available by Location"
    display_result(result)   

def max_carpark (): 
    '''             ----  Option 9 ----
    Function to display the carpark with most parking lots
    Check list of dictionaries, check for maximum value of lots available 
    '''
    max_lots = 0
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

    #printing data using loop, for key, value in dictionary
    for key, value in max_cp_info.items():
        print(f"{key}: {value}")
    result = "Option 9 Selected: Displayed Carparks available by Percentage with Address"
    display_result(result)   

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
    result = "Option 10 Selected: carpark-availability-with-address.csv written"
    display_result(result)

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
    #redfines data_dict to use carpark number as a key, address as values
    data_dict = {item["Carpark Number"]: item["Address"] for item in data_list}

    # Update dictionaries in list1 with matching addresses from data_dict
    for cp_info in list1:
        cp_no = cp_info.get("Carpark Number")
        if cp_no in data_dict:
            cp_info['Address'] = data_dict[cp_no]
    
    #checks if address exists in dictionary, if not present, adds NI
    for item in list1:
        if "Address" not in item:
            item["Address"] = "N\A"

#Global Variables
filepath = "carpark-information.csv"
data_list = read_carpark_info(filepath)    
cp_availability = []  

#GUI
import tkinter as tk
from tkinter import filedialog

def display_menu():
        #incredibly irritating GUI that took my entire weekend
        ''' 
        Function to display menu using GUI
        Makes buttons using a for loop, a list of tuples
        '''
        menu_window = tk.Toplevel(root)
        menu_window.title("Menu")

        def option3():
            #function to select a file for reading
            filepath = filedialog.askopenfilename(title="Select File")
            read_carpark_availability(filepath)  
            display_result("Option 3 Selected: Read .csv file")

        def option6():
            #function for option 6 input, this creates a new window
            input_window = tk.Toplevel(menu_window)  
            input_window.title("Input")
            
            percent_label = tk.Label(input_window, text="Enter percentage: ")
            percent_label.pack()
            percent_entry = tk.Entry(input_window)
            percent_entry.pack()
            #lambda used as anonymous function to run actual function, .get() used to get input
            confirm_button = tk.Button(input_window, text="Confirm", command=lambda: carpark_pcnt_lots(float(percent_entry.get())))
            confirm_button.pack()

        def option7():
            input_window = tk.Toplevel(menu_window)  # Create a new window for input
            input_window.title("Input")
            
            percent_label = tk.Label(input_window, text="Enter percentage:")
            percent_label.pack()
            percent_entry = tk.Entry(input_window)
            percent_entry.pack()
            #lambda used as anonymous function to run actual function, .get() used to get input
            confirm_button = tk.Button(input_window, text="Confirm", command=lambda: carpark_pcnt_lots_address(float(percent_entry.get())))
            confirm_button.pack()

        def option8():
            input_window = tk.Toplevel(menu_window)  # Create a new window for input
            input_window.title("Input")
            
            location_label = tk.Label(input_window, text="Enter location:")
            location_label.pack()
            location_entry = tk.Entry(input_window)
            location_entry.pack()
            #lambda used as anonymous function to run actual function, .get() used to get input
            confirm_button = tk.Button(input_window, text="Confirm", command=lambda: carpark_location_check(location_entry.get().upper()))
            confirm_button.pack()
                
        options = [
            ("1 - Display Total Number of Carparks", total_carpark),
            ("2 - Display All Basement Carparks", total_basement_carpark),
            ("3 - Read File", option3),
            ("4 - Total Carpark", total_carpark_availability),
            ("5 - Carpark with Lots", carpark_with_lots),
            ("6 - Carpark by %", option6), 
            ("7 - Carpark by % with Address", option7), 
            ("8 - Carpark by Location", option8),
            ("9 - Carpark with Max Lots", max_carpark),
            ("10 - Write Carpark File w/ Address", carpark_file)]
        
        for option_text, command in options:
            button = tk.Button(menu_window, text=option_text, command=command)
            button.pack(pady=5)
        
                
def display_result(result):
    '''
    Function to print what option has been run
    Result in every other function run by buttons
    '''
    result_label = tk.Label(root, text=result)
    result_label.pack()

root = tk.Tk()
root.title("S10258457C PRG Assignment GUI")

label = tk.Label(root, text="Carpark Information System", font=("Arial", 16))
label.pack(pady=10)

menu_button = tk.Button(root, text="Show Menu", command=display_menu)
menu_button.pack()

exit_button = tk.Button(root, text="Exit", command=root.quit)
exit_button.pack()

root.mainloop()    