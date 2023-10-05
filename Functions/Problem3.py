#Python Problem to Check weather a Number is strong or not.
#145 --> 1!+5!+4!
     #--> 120+24+1--> 145

def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact

def strong(num):
    temp = num
    sum = 0
    while num!=0:
        rem = num%10 # --> 4
        sum=sum+factorial(rem)
        num=num//10
    if sum==temp:
        return True 
    else:
        return False
    #return sum==temp 

number = int(input("Enter a Number :"))
n = strong(number)
print(n)
if n:  #True
    print("Number is Strong Number")
else:
    print("Number is not Strong")


math.factorial()