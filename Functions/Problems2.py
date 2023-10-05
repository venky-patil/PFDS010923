#Python Problem to Check weather a Number is Armstrong or not.
#153 --> 1**3+5**3+3**3
     #--> 153

#1634 --> 1**4   +   6**4   +   3**4 +   4**4
     #-- 1634 

def count(num):
    count=0
    while num!=0:
        count=count+1
        num=num//10
    return count


def armstrong(num):
    temp = num
    sum = 0
    digits = count(num)
    while num!=0:
        rem = num%10 # --> 4
        sum=sum+(rem**digits)
        num=num//10
    if sum==temp:
        return True 
    else:
        return False
    #return sum==temp 

number = int(input("Enter a Number :"))
n = armstrong(number)
print(n)
if n:  #True
    print("Number is Armstrong Number")
else:
    print("Number is not Armstrong")