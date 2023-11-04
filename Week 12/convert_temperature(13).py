def fahr_to_cel(fahr):
    
    cel = 5.0/9.0 * (fahr - 32)
    return cel


def cel_to_fahr(cel):
    fahr = 9.0/5.0 * cel + 32
    return fahr

def print_menu(menu_list):
    print("Temperature conversion\n")
    for i in range(len(menu_list)):
        print('[{}]{}'.format( i + 1, menu_list[i]))

menu_list = ['Celcius to Fahrenheit', 'Fahrenheit to Celcius', 'Exit']


while True:
    print_menu(menu_list)
    choice = int(input("Please enter your option: "))
    
    if choice  == 1:
        ini_temp = float(input("Enter the temperature in Fahrenheit: "))
        convert_temp = fahr_to_cel(ini_temp)
        print("The temperature in celcius is {:.1f} degrees\n".format(convert_temp))

    if choice == 2:
        ini_temp = float(input("Enter the temperature in Celcius: "))
        convert_temp = cel_to_fahr(ini_temp)
        print("The temperature in fahrenheit is {:.1f} degrees\n".format(convert_temp))
    
    if choice == 3:
        print("*EXIT*")
        break



