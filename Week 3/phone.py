path = 'C://pythonresource//'
datafile = open(path + 'StudentData.txt', 'r')

print(‘Name’ + ‘\t’ + ‘Mobile Contact’)
#1st student
student = datafile.read()
list = student.split(‘,’)
student.strip(‘\n’)
print(list[0], ‘\t’, list[1])
#2nd student
student = datafile.read()
student.strip(‘\n’)
list = student.split(‘,’)
print(list[0], ‘\t’, list[1])
file.close


