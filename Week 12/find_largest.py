def find_larger(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2

pos = ["First", "Second", "Third", "Fourth"]


n1 = int(input(f"Enter the {pos[0]} number: "))
for i in range(1,4):
    n2 = int(input(f"Enter the {pos[i]} number: "))
    n1 = find_larger(n1,n2)
print("The largest integer is", n1)