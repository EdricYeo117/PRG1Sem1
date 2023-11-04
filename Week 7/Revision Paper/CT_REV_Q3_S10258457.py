
details_list = [
    ["Sharon", "F", 33],
    ["Mic", "M", 24], 
    ["Josh", "M", 25], 
    ["Hannah", "F", 30], 
    ["Hanzel", "M", 26]
]

name_list: list[str] = ["Sharon", "Mic", "Josh", "Hannah", "Hanzel"]
height_list: list[int] = [172, 166, 187, 200, 166]
weight_list: list[float] = [59.50, 65.60, 49.80, 64.20, 47.50]
size_list = ["M", "L", "S", "M", "S"]
bmi_list: list[float] = []

for height, weight in zip(height_list, weight_list):
    bmi: float = weight / (height / 100) ** 2
    bmi_list.append(bmi)

print("Name\tWeight\tHeight\tBMI\tGender\tAge\tBMR")
for detail, bmi, size, height, weight in zip(details_list, bmi_list, size_list, height_list, weight_list):
    if detail[1] == "F":
        BMR = 655.1 + (9.6 * weight) + (1.8 * height) - (4.7 * detail[2])
    else:
        BMR = 66.47 + (13.7 * weight) + (5 * height) - (6.8 * detail[2])
    
    print(f"{detail[0]}\t{weight}\t{height}\t{bmi:.2f}\t{detail[1]}\t{detail[2]}\t{BMR:.2f}")
