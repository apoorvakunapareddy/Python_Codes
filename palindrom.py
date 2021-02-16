if __name__=="__main__":

    PALINDROM
    o(n)
    o(1) - time and space constant
    text= input("Please enter the string: ")   1
    reversetext=text[::-1] 1
    reversetext2='' 1
    for i in range(len(text)-1,-1,-1): n
        reversetext2=reversetext2+text[i] 1
    print(reversetext) 1
    print(reversetext2) 1
    if text==reversetext2: 1
        print('palindrom')
    else:
        print('Not a palindrom')


EVEN OR ODD
# o(1)
    num=int(input('please enter a number: ')) 1
    if num%2==0: 1
        print('Number is even')
    else: 
        print('Number is odd')

#AMSTRONG

    # num=int(input('please enter a number: '))
    # x=0
    # total=0
    # num2=num
    # while True:
    #     if num2<1:
    #         break
    #     else: 
    #         x=num2%10
    #         num2=num2//10
    #         print(num2)
    #         print(x)
    #         total=total+(x*x*x)
    #         print(total)
    # if total==num:
    #     print("Number is Amstrong")
    # else:
    #     print("Number is not armstrong")


# Reverse a Number

    # num=int(input('enter a number: '))
    # x=0
    # while True:
    #     if num<1:
    #         break
    #     else:
    #         x=(x*10)+num%10
    #         num=num//10
    #         # print(num,x)
    # print(x)


# Anagram

    # text1= input('please enter string1: ')
    # text2= input('please enter string2: ')
    # list1=[]
    # list2=[]
    # for i in text1:
    #     list1.append(i)
    # for i in text2:
    #     list2.append(i)

    # list1=sorted(list1)
    # list2=sorted(list2)

    # if list1==list2:
    #     print('Both are anagrams')
    # else:
    #     print('Not Anagram')


# PRIME NUMBER
    num= int(input('please enter a number'))
    list1=[]
    for i in range(2,num-1):
        list1.append(num%i)

    print(list1)
    if 0 in list1:
            print("Number is Not prime")
    else:
            print('prime')
    # for i in range(2,num):
    #     if num%1==0:
    #         print('Not prime')
    # print('prime')


# PRIME NUMBER 2

    def getnumber():
    num= int(input('Please enter a number: '))
    return num

    def primecheck(num):
        if num==2:
            return True
        elif num==1:
            return False

        for i in range(2,num):
            if num%i==0:
                return False
        return True

#  Fibanocci

def getfibanocci():
    num=int(input('please number the total number of elements in the series: '))
    list1=[]
    for i in range(0,num):
        if i ==0:
            list1.append(1)
        elif i==1:
            list1.append(list1[0])
        else:
            list1.append(list1[i-1]+list1[i-2])
    return(list1)

print(getfibanocci())


# Pangram


import string

String1=input("Please enter the String:")

# print(String2)
def pangram(string1,string2):
    string1=string1.lower()
    string1=string1.replace(' ','')
    print(string1)
    print(string2)
    if String1 in string2:
        print("It is Pangram")
    else:
        print("Nope")

String2= string.ascii_lowercase
pangram(String1,String2)


# paranthesis match


def match(ch1,ch2):
    Matchdict = { '(':')','{':'}','[':']' }
    return Matchdict[ch1]==ch2


def is_balanced(string1):
    s=Stack()
    Flag=False
    for i in string1:
        if i in ('{','[','('):
            s.push(i)
        elif i in ('}',']',')') and s.empty()==False and match(i,s.peek())==True:
            Flag=True
            s.pop()
    if s.empty()==True and Flag==True:
        return True
    else:
        return False

if __name__ == "__main__":    
    # print(is_balanced("({a+b})"))
    print(is_balanced("))((a+b}{]]")) 
    # print(is_balanced("((a+b))"))
    # print(is_balanced("))"))    
    # print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))