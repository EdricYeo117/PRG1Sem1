time = float(input('Please enter the time to be converted, in sec: '))
hours = 8600 // 3600
minutes = (8600 % 3600) // 60
seconds = 8600 % 3600 % 60
print("Time: {} hr {} min {}s".format(hours,minutes,seconds))
      
