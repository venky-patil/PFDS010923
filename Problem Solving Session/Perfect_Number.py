#Perfect Number --> If the summation of the factors of a Number is equal to original Number 

# num = 28 --> 1,2,4,7,14 --> 28

Number = int(input("Enter a Number : ")) #6
sum = 0
for i in range(1,Number):
    if Number%i==0:
        sum=sum+i 
    
if sum==Number:
    print("Number is Perfect Number")
else:
    print("Number is not Perfect Number")
