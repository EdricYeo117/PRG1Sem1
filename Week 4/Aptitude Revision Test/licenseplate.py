#Input

number_plate = input("Enter the license plate number:")

#converting 2nd and 3rd to numbers
digit2 = ord(number_plate[1].upper()) - ord('A') +1
digit3 = ord(number_plate[2].upper()) - ord('A') + 1


#sum
sum = digit2*9 + digit3*4 + int(number_plate[3])*5 + int(number_plate[4])*4 + int(number_plate[5]) *3 + int(number_plate[6])*2

#Value
remainder = sum % 19
reference_string = "AZYXUTSRPMLKJHGEDCB"

#checking if valid

if reference_string[remainder] == number_plate[-1].upper():
    print("Valid")
else:
    print("Invalid")
                     
