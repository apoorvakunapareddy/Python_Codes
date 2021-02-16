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