##Yeo Jin Rong, S10258457C, Commission Calculator

#Input

sales = float(input("Enter the sales for this month: "))

#process

if sales >= 10000:
    commission = float(sales * 0.1)
    print(commission)
else:
    commission = float(sales * 0.05)
    print(commission)
