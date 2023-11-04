#Yeo Jin Rong, S10258457C, rng calculator


import random
num1 = random.randint(0,100)
num2 = random.randint(0,100)

#input
input1 = int(input("Enter the sum of " + str(num1) + " and " + str(num2) + ":"))

if input1 == (num1 + num2):
    print("Your answer is correct!")
else:
    print("Your answer is wrong.")
    print("The correct answer is " + str(num1 + num2) + ".")
