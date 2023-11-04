file_path = "c:\PRG1\prices.txt"
drinks = ["teh peng: $1.20", "milo peng: $1.40"]


with open(file_path, "a") as file:
    for i in drinks:
        file.write(i + "\n")

file.close()
      
