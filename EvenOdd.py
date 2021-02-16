Num=int(input('Enter the number:'))
Check= int(input('Enter the check number:'))
if Num % 2 == 0:
    if Num % 4 ==0:
        print('Number multiple of 4')
    else:
        print('Even number')
else:
    print('Odd number')

if (Num%Check==0):
    print('{} is divisable by {}'.format(Num,Check))
else:
    print('{} is not divisable by {}'.format(Num,Check))