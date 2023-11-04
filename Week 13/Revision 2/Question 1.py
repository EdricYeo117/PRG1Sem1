filename = 'sales.txt'
file = open(filename, 'r')
list_unit = []

for line in file:
    temp_list = line.strip('\n').split(',')
    list_unit.append(temp_list)

file.close()

print('\n')
      

for i in range(len(list_unit)):
    print('{:<13} {:<15} {:<15}'.format(list_unit[i][0], list_unit[i][1], list_unit[i][2]))


#------------------------------------------------#

product_list = ['MacBook Air', 'MacBook Pro', 'iMac']
total_units_list = [0, 0, 0]

for i in range(len(product_list)):
    value = 0
    for j in range(len(list_unit)):
        if product_list[i] == list_unit[j][1]:
            value += int(list_unit[j][2])

    total_units_list[i] = value

#-------------------------------------------------#

print('\n {:<13} {:<15}'.format("Product", "Total Units Sold"))

for i in range(len(product_list)):
    print('{:<13} {:<15}'.format(product_list[i], total_units_list[i]))
