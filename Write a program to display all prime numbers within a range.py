# Write a program to display all prime numbers within a range.
start = int(input("enter starting number: "))
end = int(input("enter ending number: "))

print("\nprime number between ", start,"  and ", end)
for num in range(start,end + 1):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                break
            else:
                print(num)
