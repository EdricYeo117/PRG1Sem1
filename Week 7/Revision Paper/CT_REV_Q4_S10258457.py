def is_triangle_number(number):
    n = 0
    while True:
        triangular_number = (( n ** 2) + n) // 2

        if triangular_number == number:
            return n
        elif triangular_number > number:
            return None
        n += 1


number = int(input("Enter a number between 0 and 5000: "))
n = is_triangle_number(number)

if n is not None:
    print(f"{number} is a triangular number and it is the {n}th number.")
else:
    print(f"{number} is NOT a triangular number.")
             
