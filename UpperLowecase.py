String = input('Please enter the string: ')


def CaseCal(String):
    upper=0
    lower=0
    for i in String:
        if i.isupper()==True:
            upper+=1
        elif i.islower()==True:
            lower+=1
    print('No of upper case Char: {}'.format(upper))
    print("No of lower case Char: {}".format(lower))


CaseCal(String)