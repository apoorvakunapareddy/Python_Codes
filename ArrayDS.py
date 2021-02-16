
Exlist=[2200,2350,2600,2130,2190]
a=Exlist[1]-Exlist[0]
print("Extra spent in feb: "+ str(a))
b= Exlist[1]+Exlist[0]+Exlist[2]
print(b)
for i in range(0,len(Exlist)):
     if Exlist[i]==2000:
         print(i)    
print("No month with 2000")

Exlist.append(1980)
print(Exlist)
Exlist[3]=Exlist[3]+200
print(Exlist)