#Yeo Jin Rong, S10258457C, determining leap year

#input

year = int(input("Please enter the year: "))

#process

if year % 4 == 0 and year % 100 != 0:
    print ("{} is a leap year.".format (year))

elif year % 400 == 0:
        print("{} is a leap year.".format (year))

else:
    print("{} is not a leap year.".format (year))

