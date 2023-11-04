numbers = [2, 7, 11, 6, 7, 3, 17, 7, 12, 41, 8, 11, 13, 10, 15]
odd_numbers = []
count = 0

for num in numbers:
    if  num % 2 != 0:
        if num not in odd_numbers:
            odd_numbers.append(num)
            count += 1
            if count == 5:
                break

print(odd_numbers)            

