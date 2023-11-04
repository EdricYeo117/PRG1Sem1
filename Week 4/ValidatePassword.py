#Yeo Jin Rong, S10258457C, code for password validation


import re

def password_validity(password):

    if len(password) < 8:
        return "Password must be at least 8 characters long."
        
    if not re.search(r"[A-Z]", password):
        return "Password must contain at least one uppercase letter"

    if not re.search(r"[a-z]", password):
        return "Password must contain at least one lowercase letter"
    
    if not re.search(r'\d', password):
        return "Pssword must contain at least one digit"
    
    else:
        return "Password is valid"

password = input("Enter the password: ")

print(password_validity(password))

    
