# Calculate the cube of all numbers from 1 to a given number
a = int(input("enter the number :"))
sum = 0
for i in range (1,a+1):
    cube = i**3
    sum += cube
    print(sum)