number = int(input("Enter a Number : "))
count=0
while number!=0:  #Always
    count=count+1
    number = number//10
print("The Count of the digits is ",count)