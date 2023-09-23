# Prime Number --> If a number is only divisble by 1 and itself then it is a prime numbers.

number = int(input("Enter a Number :")) #3

if number>1:
    for i in range(2,6):#2,3,4,5
        if number%i==0: #-->True
            print("Number is not a Prime")
            break
    else:
        print("Number is Prime")
else:
    print("Number is  a Prime")
