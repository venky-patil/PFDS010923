#strong Number --> Summation of Factorial of the Digits  is equal to Original Number.

# 145  -->    1           +     4              +   5
#      -->    1          +     24           +   120
#      -->    1+24+120 
#      -->    145
import math 

num = int(input("Enter a Number")) #153
temp = num
sum = 0 
while num!=0:
    rem = num%10  #3
    print("Reminder is :",rem)
    sum = sum+(math.factorial(rem))  #27
    print("Sum is ",sum)
    num = num//10 #15
    print("Number Value is ",num)

if temp==sum:
    print("Number is a Strong Number ")
else:
    print("Number is not a Strong Number")