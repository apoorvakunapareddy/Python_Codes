a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#  for i in range(0,len(a)):
#      if a[i]%2==0:

# appending data using index 
b= [a[i] for i in range(0,len(a)) if a[i]%2==0]
print(b)

#  appending data using value 
b = [number for number in a if number % 2 == 0]