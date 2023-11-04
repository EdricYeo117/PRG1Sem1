#Programming I
#####################################
#            Mission 2.2            #
#           Triangle Calculator     #
#####################################
#Background
#==========
#Tom has learnt that if he knows the length of the 3 sides of a triangle,
#he is able to calculate the area by using the Heron's formula (please check
#it out in internet if you cannot remember the formula).
#Requirements
#============
#Write a Python program to calculate the perimeter and area of a triangle
#whose length of the 3 sides are entered by the user. Display the results
#in a nicely formatted string, like the following:
#    For a triangle with sides 3.0, 4.0 and 5.0
#    The perimeter is 12.00
#    The area is 6.00
#Note: values shown above are just examples
#TYPE YOUR PYTHON CODE BELOW
#===========================
#Do you need to import any module?
#Input
import math
a = float(input("Enter the 1st length of a triangle: "))
b = float(input("Enter the 2nd length of a triangle: "))
c = float(input("Enter the 3rd length of a triangle: "))
#Process
perimeter = float(a + b + c)
s = float(perimeter / 2)
area = (math.sqrt(s * (s-a) * (s-b) * (s-c)))
#Output
print("For a triangle with sides {:.1f}, {:.1f}, {:.1f}".format(a,b,c))
print("The perimeter is {:.2f}".format(perimeter))
print("The area is {:.2f}".format(area))