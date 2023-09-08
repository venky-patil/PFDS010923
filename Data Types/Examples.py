# Examples of Varibales :

x = "Praty1234a$%^&*"  #Here x is a variable and Pratyush is my Data which is stored in x variable.

print(x+"Srivastava") #Praty1234a$%^&*Srivastava

x = 10
print("x") #x

x = 10
print(x) #10

#Example of Type Function:


n=10
print(type(10)) #integer


n="Ansh"
print(type(n)) #String

n = "abc"
print(type(n)) #String


#Example of Integer Datatype

num = 1098
print(type(num)) #int


num = -98
print(type(num)) #int


num =  0
print(type(num)) #int

num = 9876543219
print(type(num)) #int


num = 1234567890123456789123456789123456789123456789
print(type(num)) #int


#Example of Float Datatypes:

num = 1.2
print(type(num)) #float

num = 0.0
print(type(num)) #float

num = -0.02313
print(type(num)) #float


num = -0.0000000000000000000000000000000000000000000000000000000000000000001
print(type(num)) #float


#Example of Complex Number

#a+bj  -->  a is real part and b is imaginary part 

num = 10+30j
print(type(num)) #complex



num = 10.0+30j
print(type(num)) #Complex


num = 30j
print(type(num)) #Complex

#Example of Complex Number with imag and real variables.

num = 1+2j
print(num.imag) #2.0


num = 2j
print(num.real) #0.0

num = 30+55.9j 
print(num.imag)  #55.9

num = 10+20j
print(num.real) #10.0

num = 33.5j  
print(num.real) #0.0


num = 10-2j  
print(num.real) #10.0

num = 10-2j  
print(num.imag) #-2.0


num = 10j
print(num) #10j


num1 = 10+20j
num2 = 1+2j
print(num1+num2) #11+22j

num1 = 10+20j
num2 = 1+2j
print(num1-num2) #9-18j


num1 = 10+20j
num2 = 1+2j
print(num1*num2) #-30+40j

# (10+20j)(1+2j)
# 10+20j+20j+40j^2
# 10+40j-40
# -30+40j

# Example of Boolean Datatype

num1 = True
print(type(num1)) #Bool

num2 = False
print(type(num2))


num2 = True+False+True+False+True+True+True
#       1  +  0  +  1 +  0  +  1 +  1 + 1
print(num2) #5

num1  = True+50.0
#        1  +50.0
print(num1) #51.0



#Example of String Datatype:

string1 = 'a'
print(type(string1)) #String

string1 = "10+20j"
print(type(string1)) #String

string1 ='''True'''
print(type(string1)) #String 


string1 ="Hi How are You I Hope Your Python Classes are Going Well"
print(type(string1))#String


x = "10.5"
print(type(x))#String

date = "08-08-2023"
print(type(x))#String


num1 = '9'
print(type(num1)) #String

num1 = "9"
print(type(num1))

password = "abAbc1234@*"