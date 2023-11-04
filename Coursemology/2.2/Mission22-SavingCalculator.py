#Programming I
#####################################
#            Mission 2.2            #
#           Saving Calculator       #
#####################################
#Background
#==========
#Tom remembers the compound interest calculator that he did in Mission 1.
#Instead of calculating the compound interest of a given principal sum after
#x number of years, he would like to calculate the number of years needed to
#reach a certain final amount with an initial savings at a fixedinterest rate.
#You may refer to the question in Coursemology for the formula
#Requirements
#============
#Write a Python program to get the input for the final amount and initial saving,
#calculate the number of years needed to reach the final amount. Assume that
#the annual interest rate is 5% and the interest is compounded monthly.
#Display the result as a smallest integer number that is just bigger than the
#result calculated. E.g. print 6, if it is bigger than 5 but less than 6.
#TYPE YOUR PYTHON CODE BELOW
#===========================
#Do you need to import any module?
#Input
#p = principal, r = annual interest rate (5), n = 12, a = final amount of money
import math
final_amount = float(input("Enter the final amount of money: "))
principal = float(input("Enter the initial amount of money: "))
rate = 0.05/12
#Process
t = math.log(final_amount / principal) / (12 * math.log(1 + rate))
time = math.floor(t) + 1
#Output
print("The number of years required to reach this amount is {}".format(time))
