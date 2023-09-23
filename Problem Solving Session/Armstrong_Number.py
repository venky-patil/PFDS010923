# Armstrong Number --> Summation of count of the Digits to the power is equal to Original Number.

# 153  -->    1           +     5              +   3
#      -->    1**3        +     5**3           +   3**3
#      -->    1+125+27 
#      -->    153

num = int(input("Enter a Number")) #153
count = len(str(num))  #len('123') #3
temp = num
sum = 0 
while num!=0:
    rem = num%10  #3
    print("Reminder is :",rem)
    sum = sum+(rem**count)  #27
    print("Sum is ",sum)
    num = num//10 #15
    print("Number Value is ",num)

if temp==sum:
    print("Number is a Armstrong Number ")
else:
    print("Number is not a Armstrong Number")


