import math

a = float(input("Enter the length of a: "))
b = float(input("Enter the length of b: "))
c = math.sqrt(pow(a,2) + pow(b,2))
print("The length of c is", c)

r = c/2
area = math.pi*pow(r,2)
print("The area of circle is", area)

