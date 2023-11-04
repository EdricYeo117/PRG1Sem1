#Programming I
#######################
#     Mission 6.1     #
#      Scrabble       #
#######################
#Background
#==========
#Tom is playing scrabble with his group of friends. He has drawn 5 letters from
#the bag. Tom wants to count the number of possible 5-letters words he can form.
#Factorial functions are frequently used to identify the number of ways to arrange
#a group of objects.
#Given the number of objects as n,
#	Factorial of n = n x (n-1) x (n-2) x (n-3) x … x 2 x 1
#	e.g. factorial of 5 = 5 x 4 x 3 x 2 x 1
#Write a Python program that prompts the user to enter the number of letters, and calculate
#the number of possible n-letters word combination that can be formed.
#Note: There is no need to consider if the words are found in a dictionary.
#Important Notes
#===============
#1) Comment out ALL input prompts before submitting.
#2) You are to complete this question with a variation of while and if statements.
#3) You MUST use the following variables
#   - number_of_letters
#   - result
#START CODING FROM HERE
#======================
#Calculate the number of possible n-letters words
def factorial(number_of_letters):
    result = 1
    while number_of_letters > 1:
        result *= number_of_letters
        number_of_letters -= 1
    return result
#Prompt user to enter the number of letters he/she has in their hands
#number_of_letters = int(input("Enter the number of letters you have: "))
#Call the function to calculate the factorial and get the result
result = factorial(number_of_letters)
#Display the output with an appropriate description
print("The number of possible", number_of_letters, "-letter word combinations is:", result)
