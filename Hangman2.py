import random
import string



def replaceletter(word,index,letter,str1):
    # print(word,index,letter)
    str2=str1[:index]+letter+str1[index+1:]
    return str2
 
 
def main():
    f= open('Sowpods.txt','r')
    text=f.read()
    list1=text.split('\n')
    myword=random.choice(list1)
    print(myword)
    str1=''
    str2=''
    list1=[]
    for i in myword:
        str1=str1+'_'
    counter=0
    print(str1)
    while True:
            if counter==6:
                print('Game over')
                repeat=input('Do yopu want to play again Y/N: ')
                if repeat=='Y':
                    main()
                else:
                    print('Thank you for playing')
                    exit()
            elif str1==myword:
                print('Guessed it correct')
                repeat=input('Do yopu want to play again Y/N: ')
                if repeat=='Y':
                    main()
                else:
                    print('Thank you for playing')
                    exit()
            letter=input("please guess a letter in capital : ")
            if letter in myword:
                for i in range(0,len(myword)):
                    if myword[i]==letter:
                        str1=replaceletter(myword,i,letter,str1)
                        # str1=str1+letter
                print(str1)
            else:
               
                if letter not in list1:
                    counter=counter+1
                list1.append(letter)
                print(6-counter,'Incorect guess left')

if __name__ == "__main__":
   main() 

