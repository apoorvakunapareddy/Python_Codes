
if __name__=='__main__':
    bday={'Appu':'5Sept92','Praneeth':'29Oct91','Niki':'25Sept93','Abhi': '11Jul91', 'Prateek': '9Jul93'}
    print('Welcome to Bday dictonary, we know bdays of:')
    for i in bday:
        print(i)
    name=input("Who's bday do you want to see: ")
    if name in bday.keys():
        print(bday.get(name))
    else:
        print('name not in dictionary')
