#functions

def dis_menu(menu_list):
    print('\nOrders')
    for i in range(len(menu_list)):
        print('[{}]{}'.format(i+1, menu_list[i]))

def dis_prices(prices_dict):
    print('\nItem List')
    print("{:10s} {:6s}".format("Item", "Price"))
    print("{:10s} {:6s}".format("----", "-----"))
    for j in prices_dict:
        print("{:10s} ${:0.2f}".format(j.capitalize(), prices_dict[item]))

def dis_orders(orders_dict):
     print("{:10s} {:6s}".format("Item", "Quantity"))
     print("{:10s} {:6s}".format("----", "-------"))
     total = 0.0
     for k in orders_dict:
         print("{:10s} ${:0.2f}".format(k.capitalize(), prices_dict[item]))
         total += (orders_dict[item] * prices_dict[item])
     print("Total cost = ${:.2f}".format(total))

#process

prices_dict = {'chicken' : 8.50,\
          'steak' : 13.80,\
          'fish' : 9.80,\
          'pasta' : 9.50,\
          'coffee' : 2.50,\
          'tea' : 1.80,\
          'water' : 0.50}

orders_dict = {}
menu_list = ["Add order", "Summarize orders", "Quit"]

while True:
    dis_menu(menu_list)
    choice = int(input("Your choice?"))

    #choice1
    if choice == 1:
        dis_prices(prices_dict)
        food = input("Your order? ").lower()

        if food in prices_dict:
            quan = int(input("How many sets? "))
            if food not in orders_dict:
                orders_dict[food] = quan
            else:
                orders_dict[food] += quan
            print("{} sets of {} ordered.".format(quan, food))
        else:
            print(food + " is not available.")


#choice2
    elif choice == 2:
        dis_orders(orders_dict)
    
    elif choice == 3:
        print("* Exit *")
        break

    else:
        print('* Invalid input *')

print('\n *** Thank you ***')

