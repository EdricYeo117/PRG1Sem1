
page = [0,50,100,150,200,250,300,350,400,450,500]
def calculate_charge(pages):
    cost = 0
    if pages <= 100:
        cost = pages * 0.03

    if pages <= 300:
        cost = 100 * 0.03 + (pages - 100) * 0.02 
    
    else:
        cost = 100 * 0.03 + 200 * 0.02 + (pages - 300) * 0.01

    return cost

def calculate_gst(cost):
    charge = cost * 1.07
    return charge

print("{:<12}{:>9}{:>21}".format("Pages","Charge($)","Include gst($)"))
for i in page:
    cost,charge = calculate_charge(i),calculate_gst(calculate_charge(i))
    print(f"{i:<12}{cost:>9.2f}{charge:>21.2f}")

