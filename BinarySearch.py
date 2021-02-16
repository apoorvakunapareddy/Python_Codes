def sort1(list1):
    list1.sort(key=int)
    return list1

def search1(list1,num):
    for i in list1:
        # print(i,num)
        if int(i)==num:
            return True
    return False
    
# def midvalue(list1):
#     if len(list1)%2==0:
#         mid=int(len(list1)/2)
#     else:
#         mid=int((len(list1)+1)/2)
#     return mid

def binarysearch(list1,num):
    while list1:
        i=int(len(list1))
        mid=int((len(list1)/2))
        
        # print(mid,list1[mid])
        if num<=int(list1[mid]):
            if num==int(list1[mid]):
                return True
            else:
                print(list1[0:mid])
                return binarysearch(list1[0:mid],num)

        else:
            if num==int(list1[mid]):
                return True
            else:
                print(list1[mid+1:i])
                return binarysearch(list1[mid+1:i],num)
    
    return False  

def binarysearchitr(list1,num):
    start=0
    end=len(list1)-1

    # print(list1[start],list1[end])
    while True:
        mid=int((start+end+1)/2)
        print(mid)
        if mid<start or mid>end or mid<0:
            return False

        if int(list1[mid])==num:
            return True

        elif num <int(list1[mid]):
            print(list1[0:mid])
            end=mid-1
            print(end)
        else:
            # print(list1[mid:end])
            start=mid+1
    



if __name__=="__main__":
    str1=input('list elements with space: ')
    lst= str1.split()
    print(sort1(lst))
    num=int(input("Enter the value you are looking for: "))
    # final=search1(lst,num)
    # final=binarysearch(lst,num)
    final=binarysearchitr(lst,num)
    # print(final)
    if final == True:
        print("number is in list ")
    else:
        print("number is not in the list")
