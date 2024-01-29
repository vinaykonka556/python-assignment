 #Calculate the sum of all numbers from 1 to a given number.
num= int(input("enter the number :"))
sum = 0
for i in range(1,num+1):
     sum = sum+i
     i=i+1
print("sum = ", sum)