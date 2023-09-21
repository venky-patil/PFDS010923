#Factorial of a Number

# 5! --> 5*4*3*2*1

# 8! --> 8*7*6*5*4*3*2*1

number = int(input("Enter A Number : "))
fact = 1
for i in range(1,number+1): 
    fact=fact*i
print(fact)

