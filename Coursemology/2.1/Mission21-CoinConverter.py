#Programming I
#####################################
#            Mission 2.1            #
#           Coin Converter          #
#####################################
#Background
#==========
#Tom has 2 50-cent coins, 4 20-cent coins, 6 10-cent coins and 9 5-cent coins.
#He would like calculate the total amount in dollars.
#Requirements
#============
#Develop a pseudocode and Python program to solve the following problem:
#   -Given a number of 50-cent coins, 20-cent coins, 10-cent coins
#    and 5-cent coins, calculate the amount in dollars, print the
#    output with proper description and the amount in proper format
#Important Notes
#===============
#1) Include the pseudocode that you have developed as comments at the
#   beginning of your program.
#2) You MUST (at least) use the following variables:
#   - cent50 (number of 50-cent coins)
#   - cent20 (number of 20-cent coins)
#   - cent10 (number of 10-cent coins)
#   - cent5  (number of 5-cent coins)
#TYPE YOUR PSEUDOCODE BELOW AS COMMENTS
#======================================
#Prompt for amount of 50 cent coins
#Get amount of 50 cent coins (a)
#Prompt for amount of 20 cent coins
#Get amount of 20 cent coins (b)
#Prompt for amount of 10 cent coins
#Get amount of 10 cent coins (c)
#Prompt for amount of 5 cent coins
#Get amount of 5 cent coins (d)
#Calculate total amount in total = 0.5*a + 0.2*b + 0.1*c + 0.05*d
#Display amount in format
#
#TYPE YOUR PYTHON CODE BELOW
#===========================
#Input
cent50 = int(input("Enter amount of 50 cent coins: "))
cent20 = int(input("Enter amount of 20 cent coins: "))
cent10 = int(input("Enter amount of 10 cent coins: "))
cent5 = int(input("Enter amount of 5 cent coins: "))
#Process
dollars = cent50 * 0.50 + cent20 * 0.20 + cent10 * 0.10 + cent5 * 0.05
#Output
print("Total amount in dollars: ${}".format(dollars))
