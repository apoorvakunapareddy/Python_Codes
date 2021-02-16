from datetime import datetime
name=input('enter your name')
age=int(input('Enter your age'))
Copies= int(input('Enter number of copies'))

currentYear= datetime.now().year 
CenturyYear= currentYear-age +100

for i in range(0,Copies):
  print(name + '\t' +'will be 100 in'+ '\t'+ str(CenturyYear))
