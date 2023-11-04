#Week15 Part 2 Activity 1 , Jason Ng, S10262552
import re

email = input('Please enter your email address: ')

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

def isValid(email):
    if re.fullmatch(regex, email):
        print('Valid email')
    else:
        print('Invalid email')

isValid(email)
