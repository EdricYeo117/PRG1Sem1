#Programming I
###############################
#       Mission 2.1           #
#    Energy Cost Calculator   #
###############################
#Background
#==========
#Ever wonder the energy cost of running an appliance or electronic device?
#Here is a simple calculation to get that figure.
#Step 1:
#Monthly electricity consumption =
#   (Power rating [Watts] of device * Number of hours used per day)/1000
#Step 2:
#Cost = Monthly electricity consumption * Electricity tariff
#                                         ($0.2743 as of April 2023 for SP group)
#Laptop computers may peak at a maximum draw of only 60 watts,
#whereas common desktops may peak around 175 watts.
#Requirements
#============
#1) Write pseudocode for the Energy Cost Calculator.
#   The solution should prompt user for the power rating of a device and the
#   number of hours used per day. After which, display the calculated cost in
#   4 decimal places.
#2) Code the Python program base on the pseudocode that you have developed.
#Important Notes
#===============
#1) Include the pseudocode that you have developed as comments at the
#   beginning of the next section.
#2) You MUST (at least) use the following variables:
#   - power_rating
#   - hours
#TYPE YOUR PSEUDOCODE BELOW AS COMMENTS
#======================================
#Prompt numbers of hours used per day
#Get hours used per day
#Prompt power rating of device in watts
#Get power ration of device 
#Calculate the monthly electricity consumption = power rating * number of hours
#Calculate total cost = monthly electricity consumption * electricity tariff
#TYPE YOUR PYTHON CODE BELOW
#===========================
#Input
hours = float(input("Enter the number of hours used on device: "))
power_rating = float(input("Enter the power rating of device: "))
#Process
monthly_consumption = hours/1000 * power_rating
electricity_tariff = 0.2743
cost = monthly_consumption * electricity_tariff
                
        
#Output
print("Monthly cost: ${}".format(cost))
