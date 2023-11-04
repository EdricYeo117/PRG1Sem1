prices = [ ["kopi", 0.4], 
           ["teh", 0.4], 
           ["milo", 0.5], 
           ["soft drinks", 1.20] ]



file_path = "c:\PRG1\prices.txt"

with open(file_path, "w") as file:
    for drink in prices:
        line = "{} : ${:.2f}".format(drink[0], drink[1])
        file.write(line + "\n")


