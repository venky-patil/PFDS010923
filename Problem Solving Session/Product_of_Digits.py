number = int(input("Enter a Number : "))#1234 --> 24
product = 1
while number!=0:
    rem = number%10  
    print("Reminder is ",rem)
    product=product*rem
    print("Product is ",product)
    number=number//10
    print("Number Value is",number)
print("Product of Digits is :",product)
