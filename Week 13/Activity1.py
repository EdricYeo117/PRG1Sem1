#dictionaries
colors_dict = {}
newcolors_dict = {}

#open csv in read mode
filename = 'colors.csv'
file = open(filename, 'r')

#for loop to read data
for line in file:
    print(line)
    line = line.strip('\n')
    data_list = line.split(',')
    print(data_list)
    colors_dict[data_list[0]] = data_list[1]

file.close()


#for loop to add things to dictionary

for name in colors_dict:
    color = colors_dict[name]

    if color in newcolors_dict:
        name_list = newcolors_dict[color]

    else:
        name_list = []

    name_list.append(name)
    newcolors_dict[color] = name_list

#output
print("\nColors Dict\n",colors_dict)
print("Length of Dict:",len(colors_dict))
print("\nNew Colors: \n",newcolors_dict)
print("Length of Dict: ",len(newcolors_dict))

