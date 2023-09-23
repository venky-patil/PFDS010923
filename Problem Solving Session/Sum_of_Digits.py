number = int(input("Enter a Number : "))#123 --> 6
sum = 0
while number!=0:
    rem = number%10  #3
    print("Reminder is ",rem)
    sum=sum+rem
    print("Sum is ",sum)
    number=number//10
    print("Number Value is",number)
print("Sum of Digits is :",sum)


