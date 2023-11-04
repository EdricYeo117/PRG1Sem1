#input
L = float(input("What is your desired loan amount?"))
A = float(input("What is your annual income?"))
C = float(input("What is the total value of your current loans?"))
S = float(input("What is the total of your savings?"))
Y = float(input("How many years do you want to pay back this loan?"))

#process
Interest_Rate = ((L + C)/(S + A * Y)) * 100
print("Your interest rate is {:.1f}%".format(Interest_Rate))
