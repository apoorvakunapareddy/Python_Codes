def piglatin():
    word=input('please enter the word: ')
    text=''
    for i in range(0,len(word)-1):
        if word[0] in ('a','e','i','o','u'):
            p=word+'ay'
            return p
        else:
            text=text+word[0]
            word=word[1:]+text
            # print(text)
            # print(word)
    return word      


print(piglatin())
        