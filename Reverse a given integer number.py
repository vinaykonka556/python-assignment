# Reverse a given integer number. 
def reverse_signed(num):
    sum=0
    sign=1
    if num<0:
        sign=-1
        num=num*-1
        while num>0:
            rem=num%10
            sum=sum*10+rem
            num=num//10
        if not -214783648<sum<214783647:
                return 0
        return sign*sum
        
print(reverse_signed(-123))