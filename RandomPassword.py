import random, string

def main():
    a = ''.join(random.choice(string.ascii_uppercase+string.ascii_lowercase+string.digits) for i in range(random.randint(8,16)))
    return a

if __name__=="__main__":
    a=input('How strong password do you want, enter strong or weak: ')
    if a =='strong':
        print(main())
    else:
        list1=['password12','harry12','July04','Sample34','Pearl09','Random45']
        b=''.join(random.choice(list1) for i in range(random.randint(1,2)))
        print(b)