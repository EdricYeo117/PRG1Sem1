

num_list = [10, -13, 50, 5, 7, 65, -40, 44, 30]

import math

def get_extremes(num_list):
    largest = -math.inf
    smallest = math.inf
    for i in num_list:
        if i < smallest:
            smallest = i
        elif i > largest:
            largest = i
    return smallest, largest


smallest, largest = get_extremes(num_list)

print(smallest, largest)
