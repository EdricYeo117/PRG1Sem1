file_path = r'c:\PRG1\todolist.txt'

with open(file_path, 'r') as file:
    for line in range(3):
        line = file.readline().strip()
        print(line)

