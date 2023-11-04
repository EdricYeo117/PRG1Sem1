file_path = r"C:\Users\User\Desktop\Week 6 code\temperature.txt"
temperatures = []
with open(file_path, "r") as file:
    for data in file.read().split(","):
        temperatures.append(float(data.strip()))
    
for temperature in temperatures:
    if temperature > 29:
        print("{:.1f} ** higher than 29!!".format(temperature))

    else:
        print(f"{temperature:.1f}")
    


total_temp = sum(temperatures)
average = total_temp/ len(temperatures)
print("\nNumber of readings:", len(temperatures))
print("Average temperature: {:.2f}".format(average))


    


