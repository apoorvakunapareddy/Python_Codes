import random
import string
def promt():
    fname=input('Please enter your firstname: ')
    lname=input('Please enter your Lastname: ')
    username=fname +''.join(random.choice(lname+string.digits) for i in range(3))
    return username

print(promt())
