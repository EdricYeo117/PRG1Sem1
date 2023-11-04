def power(x, n):
    return x ** n

x = int(input("Enter the base integer: "))
n = int(input("Enter the exponent: "))

print(f"The result of {x} with exponent {n} is {power(x, n)}")
