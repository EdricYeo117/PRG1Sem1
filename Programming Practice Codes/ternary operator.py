def is_adult(age):
    if age > 18:
        return True
    else:
        return False
def is_adult2(age):
    return True if age > 18 else False
age = int(input("Enter your age"))
check_age = is_adult2(age)
print(check_age)