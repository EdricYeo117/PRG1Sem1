#Programming I
#####################################
#            Mission 2.1            #
#    Compound Interest Calculator   #
#####################################
#Background
#==========
#Tom won a lottery amounting to $10000, and he is deciding if he should
#deposit it into a bank account to accumulate interest.
#Tom wishes to find out how much he will have in the bank account after
#a specified number of years, given his input.
#Requirements
#============
#1) Write pseudocode that sets the principal amount of $10000 to variable p,
#   annual nominal interest rate of 8% to variable r, number of times the
#   interest is compounded per year of 12 to variable n. The number of years
#   that the money will be compounded, t, is given by the user. Calculate
#   and print the final amount (up to 3 decimal places) after t years.
#   Note: Refer to the question in Coursemology for the formula.
#2) Code the Python program base on the pseudocode that you have developed.
#Important Notes
#===============
#1) Include the pseudocode that you have developed as comments at the
#   beginning of the next section.
#2) You MUST (at least) use the following variables:
#   - P (principal amount)
#   - r (annual nominal interest rate [as a decimal])
#   - n (number of times the interest is compounded per year)
#   - t (number of years)
#TYPE YOUR PSEUDOCODE BELOW AS COMMENTS
#======================================
#Prompt for amount of years
#Get number of years (t)
#Get principal amount is $10000
#Get interest set to 8.0%
#Get number of times the interest is compounded per year is 1
#Calculate final amount with compound interest = 10000(1 + 8.0)**t
#Display final amount after (t) years
#TYPE YOUR PYTHON CODE BELOW
#===========================
#Input
t = float(input("Enter the amount of years to accumulate interest: "))
#Process
p = float(10000)
r = float(0.8)
n = int(1)
total = float(10000*(1 + 0.8)**t)
#Output
print("Final amount of {:.4f} after {} years".format(total, t))
