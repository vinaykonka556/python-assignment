#write a function given number is even or odd 
def typeOfNumber(num):
    if num %2==0:
        print("Given number is Even number")
    else:
        print("Given number is Odd number")
num=int(input("Enter the number"))
result=typeOfNumber(num)


#write a func which contains some number as arg and print square of that numbers

def squareOfNumber(numbers):
    for num in numbers:
        square= num ** 2
        print(f"the square of {num} is {square}")
numbers=[2,4,5,6,7,8]
squareOfNumber(numbers)