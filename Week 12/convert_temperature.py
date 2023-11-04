def convert_temperature(c):
    farenheit = (c * 9//5) + 32
    return farenheit

c = int(input("Enter the temperature in degree celcius: "))
converted_temp = convert_temperature(c)
print("The temperature is equivalent to {:.2f} farenheight".format(converted_temp))

