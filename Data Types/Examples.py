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
print(type(password))


#Example of List Datatype:

list1 = [1,9.5,"Java",10+20j,True]
print(type(list1)) #list
print(list1[2])  #Java
print(list1[4])  #True
list1[2] = "Python"
print(list1)


#Example of Tuple Datatype:

tuple1 = (1,9.5,"Java",10+20j,True)
print(type(tuple1)) #tuple
print(tuple1[3])#10+20j
print(tuple1) #(1, 9.5, 'Java', (10+20j), True)
#tuple1[2] = "C++"
#print(tuple1) #Error


#Example of Set Datatype:

set1 = {10,20,98.5,10,20,"Hi"}
print(type(set1)) #Set
print(set1) #{10, 'Hi', 20, 98.5}
set1.add("Java")
print(set1) #{98.5, 10, 'Hi', 20, 'Java'}


#Example of Dictionary Datatype:

dict1 = {"name":"Pratyush" , "College":"Edyoda Digital University","Batch":"DS010923",10:20,True:False,"name":"Aman"}
print(type(dict1)) #Dictionary
print(dict1)
print(dict1["name"]) #Aman
print(dict1["College"]) #"Edyoda Digital University"
dict1["Batch"] = "PF010923"
dict1["name"] = "Ayush"
print(dict1) #{'name': 'Aman', 'College': 'Edyoda Digital University', 'Batch': 'PF010923', 10: 20, True: False}


#Conversion of Float Datatype to Integers --> Possible

num = 10.5
print(type(num))
print(num)
con = int(num)
print(type(con))
print(con)


#Conversion of Complex Datatype to Integer --> Not Possible

num = 10+20j
print(type(num)) #complex
print(num) #10+20j
#con = int(num)
#print(type(con)) #Error

#Conversion of Boolean Datatype to Integer --> Possible

num = True
print(type(num)) #bool
print(num) #True
con = int(num)
print(type(con)) #integer
print(con) #1

num = False
print(type(num)) #bool
print(num) #False
con = int(num)
print(type(con)) #integer
print(con) #0


#Conversion of String to Integer Datatype --> Possible/Not Possible

num = "10"
print(int(num)) #10

# num = "10.5"
# print(int(num)) #Error 

# num = "Hi"
# print(int(num)) #Error

# num = "10+20j"
# print(int(num)) #Error

#Conversion of List Datatype to Integer Datatype --> Not Possible 

# num = [10,20,30,40,50]
# print(int(num)) #Error

# Conversion of Tuple Datatype to Integer Datatype --> Not Possible 

# num = (10,20,30,40,50)
# print(int(num)) #Error



# Conversion of Set Datatype to Integer Datatype --> Not Possible 

# num = {10,20,30,40,50}
# print(int(num)) #Error


# Conversion of Dictionary Datatype to Integer Datatype --> Not Possible 

# num = {10:20,20:30,30:40,40:50,50:60}
# print(int(num)) #Error


#Conversion of Integer Datatype to Float --> Possible

num = 10
print(float(num)) #10.0


#Conversion of Complex Datatype to Float --> Not Possible

# num = 10+20j
# print(float(num)) #Error

# Conversion of Boolean Datatype to Float --> Possible 

# num = True
# print(float(num)) #1.0

# num = False 
# print(float(num))#0.0


#Conversion of String Datatype to Float --> Possible/Not Possible

num = "10"
print(float(num)) #10.0

num = "10.5"
print(float(num)) #10.5

# num = "Hi"
# print(float(num)) #Error

# num = "10+20j"
# print(float(num)) #Error

# num = "10Hi"
# print(float(num)) #Error


# Conversion of List Datatype to Float Datatype --> Not Possible 

# num = [10,20,30,40,50]
# print(float(num)) #Error


# Conversion of Tuple Datatype to float Datatype --> Not Possible 

# num = (10,20,30,40,50)
# print(float(num)) #Error



# Conversion of Set Datatype to float Datatype --> Not Possible 

# num = {10,20,30,40,50}
# print(float(num)) #Error


# Conversion of Dictionary Datatype to float Datatype --> Not Possible 

# num = {10:20,20:30,30:40,40:50,50:60}
# print(float(num)) #Error



#Conversion of Integer Datatype to Complex --> Possible

num = 10
print(complex(num)) #10+0j


#Conversion of float Datatype to Complex --> Possible

num = 10.5
print(complex(num)) #10.5+0j

#Conversion of Boolean Datatype to Complex -->Possible

num = True 
print(complex(num)) #1+0j


#Conversion of String Datatype to Complex --> Possible/Not Possible.


num = "10"
print(complex(num)) #10+0j

num = "10.5"
print(complex(num)) #10.5+0j

# num = "Hi"
# print(int(num)) #Error

# num = "10+20j"
# print(int(num)) #10+20j

# num = "10Hi"
# print(int(num)) #Error


# Conversion of List Datatype to Complex Datatype --> Not Possible 

# num = [10,20,30,40,50]
# print(complex(num)) #Error


# Conversion of Tuple Datatype to complex Datatype --> Not Possible 

# num = (10,20,30,40,50)
# print(complex(num)) #Error



# Conversion of Set Datatype to complex Datatype --> Not Possible 

# num = {10,20,30,40,50}
# print(complex(num)) #Error


# Conversion of Dictionary Datatype to complex Datatype --> Not Possible 

# num = {10:20,20:30,30:40,40:50,50:60}
# print(complex(num)) #Error



#String Conversion --> We can convert any Datatype or any data in the form of String.


num = 10
print(str(num))#'10'

num=10.5
print(str(num))#'10.5'

num = 10+20j
print(str(num))#'10+20j'

num = True
print(str(num))#'True'

num = [10,20,30,40]
print(str(num)) #'[10,20,30,40]'

num = (10,20,30,40)
print(str(num)) #'(10,20,30,40)'

num = {10,20,30,40}
print(str(num)) #'{10,20,30,40}'

num = {10:20,20:30,30:40,40:50}
print(str(num)) #'{10:20,20:30,30:40,40:50}'


#Example of Boolean Conversion:

num = 0
print(bool(num))#False

num = 0.0
print(bool(num)) #False

num = 0.00000000000000000000000000000000000000000000001
print(bool(num)) #True

num = "0"
print(bool(num))#True


num = ""
print(bool(num)) #False


#Conversion of List To Tuple --> Possible

num = [10,20,30,40,50]
print(tuple(num))#(10,20,30,40,50)

#Conversion of List To Set --> Possible

num = [10,20,30,40,50,10,20]
print(set(num))#{10,20,30,40,50}

#Conversion of List To Dictionary --> Not Possible 

# num = [10,20,30,40,50]
# print(dict(num)) #Error

#Conversion of Tuple to List --> Possible 

num = (10,20,30,40,50)
print(list(num))#[10,20,30,40]

#Conversion of Tuple to Set --> Possible 

num = (10,20,30,40,50,10,20)
print(set(num))#{10,20,30,40,50}

#Conversion of Tuple To Dictionary --> Not Possible 


# num = (10,20,30,40,50)
# print(dict(num)) #Error

#Conversion of Set to List --> Possible 

num = {10,20,30,40,50}
print(list(num)) #[10,20,30,40,50]

#Conversion of Set to Tuple --> Possible 

num = {10,20,30,40,50}
print(tuple(num)) #(10,20,30,40,50)


#Conversion of Set to Dictionary --> Not Possible 

# num = {10,20,30,40,50}
# print(dict(num)) #Error


#Conversion of Dictionary to List ---> Possible

num = {10:20,20:30,40:50}
print(list(num))#[10,20,40]


#Conversion of Dictionary to Tuple ---> Possible

num = {10:20,20:30,40:50}
print(tuple(num))#(10,20,40)

#Conversion of Dictionary to Set ---> Possible

num = {10:20,20:30,40:50}
print(set(num))#{10,20,40}



#Conversion of String to List --> Possible 

num = "Hi How Are You"
print(list(num)) #['H', 'i', ' ', 'H', 'o', 'w', ' ', 'A', 'r', 'e', ' ', 'Y', 'o', 'u']

#Conversion of String to Set --> Possible 

num = "Hi How Are You"
print(set(num)) #{' ', 'w', 'A', 'H', 'Y', 'e', 'o', 'r', 'i', 'u'}


#Conversion of String to Tuple--> Possible 

num = "Hi How Are You"
print(tuple(num)) #('H', 'i', ' ', 'H', 'o', 'w', ' ', 'A', 'r', 'e', ' ', 'Y', 'o', 'u')

#Conversion of String to Dictionary --> Not Possible

num = "Hi How Are You"
print(dict(num))  #Error