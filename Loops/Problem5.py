#Python Program to Find Factorial of a Number Using For Loop.

# 5! --> 5*4*3*2*1

number = int(input("Enter Number : ")) #3
fact = 1
for i in range(1,number+1,1): #1,2,3
    fact=fact*i   #--> fact = 1*1=1 , fact = 1*2 = 2 , fact = 2*3 = 6
print(fact) #6



#Python Program to Find Factorial of a Number Using While Loop.
number = int(input("Enter Number : ")) #3
fact=1
i=1
while i<number+1:  #1<4:            2<4:           3<4:                4<4:  #False
    fact=fact*i    #fact = 1*1=1    fact = 1*2=2   fact = 2*3=6
    i=i+1          #i = 2           i = 3          i = 4

print(fact)


