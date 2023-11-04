
menu = ['Feed','Play','Rest','Status']
stats = [3,3,3]
title = ['hungry','happiness','energy']
msg = ['Nom nom nom','XD','Zzzzz']

print("Digipet")

while True:
    print(f"(1) {menu[0]}\n(2) {menu[1]}\n(3) {menu[2]}\n(4) {menu[3]}")
    option = int(input("Please select an option: "))

    if option == 1:
        print(msg[option - 1])
        stats[option - 1] += 1
        stats[1] -= 1
        stats[2] -= 1
        
    if option == 2:
        print(msg[option - 1])
        stats[option - 1] += 1
        stats[0] -= 1
        stats[2] -= 1
        
    if option == 3:
        print(msg[option - 1])
        stats[option - 1] += 1
        stats[0] -= 1
        stats[1] -= 1

    if option == 4:
        for i in range(3):
            health = "*" * stats[i] + "." * (5 - stats[i])
            print(f"{title[i]:<10}",health)
        
