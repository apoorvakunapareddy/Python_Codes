String= input("Enter the String: ")

print(String)
print(String[::-1])
#  Using list slicing funtions
if String==String[:: -1]:
 print("Palendrom")

#  Using for loops
x=''
for i in range(len(String)):
   x+= String[len(String) -1 -i]

if String==x:
  print('Palendrom 2')
else:
    print('Not Palendrom')