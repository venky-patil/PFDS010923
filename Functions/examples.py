# Examples of Predefined Functions 
# =======================================

# id()   --> To Get Memory Location of an Object 
# ======================================================

x = 10
print(id(x))

# print()--> To Display the Output on the Console
#=========================================================
x = 10
print(x)


# len()  --> To Get Number of Elements/Character of Sequence Datatype 
#==========================================================================

x = [10,20,30,40]
print(len(x))


# type() --> To Get the Type of an Object 
#==============================================

x = [10,20,30,40]
print(len(x))

# sum()  --> To Get the Sum of all the Elements of a List,Set,Tuple.
#=====================================================================

x = [10,20,30,40]
print(sum(x))

# max()  --> To Get the Maximum Value of a Sequence
#====================================================

x = [10,20,30,40]
print(max(x))

# min()  --> To Get the Minimum Value of a Sequence.
#======================================================

x = [10,20,30,40]
print(min(x))


# Example of User Defined Functions - 1
# =======================================

def Subtraction(a,b):
    result = a-b
    return result

print(Subtraction(10,20))



# Example of User Defined Functions - 2
# =======================================

def Subtraction(a,b,c):  #Function Declaration
    result = a-b       #Function Definition
    print(result) 

print(Subtraction(10,20,30))  #Function Calling


# Example of User Defined Functions - 3
# =======================================

def Calculator(a,b): #a,b are Formal Parameter
    add = a+b 
    sub = a-b 
    div = a/b 
    fdiv = a//b 
    mod = a%b 
    return add,sub,div,fdiv,mod #Internally Python will pack all these things as a Tuple Elements

print(Calculator(20,10)) #20,10 Actual Parameter


# Example of User Defined Functions - 4
# =======================================

def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i 
    return fact
    print("Hi")
    print("Hello")
    
print(factorial(5))
    

# Example of Positional Arguments-1
# ==================================

def add(a,b,c,d):
    return a,b,c,d,a+b+c+d  #(10,20,30,40,100)

print(add(10,20,30,40))



# Example of Positional Arguments-2
# ==================================

def add(a,d,c,b):
    return a,b,c,d,a+b+c+d  #(10,40,30,20,100)

print(add(10,20,30,40))


# Example of Keyword Argument 
# =============================

def Interest(p,r,t):
    print("Principle is",p)#1000
    print("Rate is",r) #2
    print("Time  is",t) #4
    SI = (p*r*t)//10
    return SI

print(Interest(r=2,t=4,p=1000))


# Example of Default Argument:
# =============================

def create_bank_account(name,aadharno,mob,balance=0):
    print("Customer Name :",name)
    print("Aadhar No :",aadharno)
    print("Mobile No :",mob)
    print("Customer Balance :",balance)
    return ""

print(create_bank_account("Pratyush",987654321,98765432,100))

print(create_bank_account("Ansh",987654300,98765432))


# Example of *args 
# ==================

def sum(*n):    
    print(type(n), n)
    temp = 0
    for i in n:
        temp=temp+i 
    return temp

print(sum())
print(sum(10))
print(sum(10,20))
print(sum(10,20,30))
print(sum(10,20,30,40))


# Example of **args 
# ==================

def sum(**n):    
    print(type(n), n)
    return "Dictionary Found"

print(sum(x=10))
print(sum(y=10))
print(sum(z=10,a=20))
print(sum(b=10,c=20,d=30))
print(sum(f=10,g=20,h=30,k=40))



# Example of Global Variable 
# =============================

pi = 22/7  #Global Variable
def area_of_circle(radius):
    return pi*radius**2

print(area_of_circle(10))

# Example of Local Variable 
# =============================

def perimeter_of_circle(radius):
    pi = 22/7                         #local Variable
    return pi*radius**2

print(perimeter_of_circle(10))


# Example of Global Scope 
# =========================

a=10 #GLobal
b=20  #Global
def check(c,d):
    print(a,b,c,d)
    return "Global Scope Checked"

print(check(100,200))
print(a,b)


# Example of Local Scope
# ========================

x=10 #Global
y=20 #Global 
def trim():
    z=99   #Local
    d=198  #Local
    print(x)
    print(y)
    print(z)
    print(d)
    return ""
print(trim())
# print(d)
# print(z)


# Example of Priority of Variables 
# ================================

a = 10
b = 20 
c = 30
def dummy():
    a=100
    b=200
    print(a)
    print(b)
    print(c)

    return ""

print(dummy())
print(a)
print(b)   

# Example of Global keyword -1
# ============================


az=10 
def f1():
    print(az)
    return ""

def f2():
    global az
    az=777
    print(az)
    return ""


print(f2())
print(az)



# Examples of Global Keyword  - 2
# ================================

az=10 
def f1():
    print(az)
    return ""

def f2():
    global az
    az=777
    print(az)
    return ""

print(f1())
print(az)




# Examples of Global Keyword  - 3
# ================================

abc=999 
def f1():
    print(abc+100)
    return ""

def f2():
    global abc
    abc=900
    print(abc+800)
    return ""

def f3():
    print(abc)
    return "" 

print(f1()) #1099
print(f3())#999


# Examples of Global Keyword  - 4
# ================================

abc=999 
def f1():
    print(abc+100)
    return ""

def f2():
    global abc
    abc=900
    print(abc+800)
    return ""

def f3():
    print(abc)
    return "" 

print(f1())  #1099
print(f2())#1700
print(f3())#900

# Examples of Global Keyword  - 5
# ================================

abc=999 
def f1():
    print(abc+100)
    return ""

# def f2():
#     print(abc)
#     global abc 
#     abc=900
#     print(abc+800)
#     return ""

# def f3():
#     print(abc)
#     return "" 

# print(f1()) 
# print(f2())
# print(f3())


# Example of Nested Functions 
# =============================

def add(x,y):
    def sub(x,y):
        return x-y 
    return x+y,sub(x,y)

print(add(10,20))



def add(a,b):
    return a+b 
print(add(10,20))


# Example of Nested Functions - 3 
# ================================

def outer():
    print("Inside Outer Function")
    def inner():
        return "Inside Inner Function"
        print("Inner Function")
    return "Outer Function Executed",inner()

print(outer())

# Example of Nested Functions - 4
# ================================

def outer():
    print("Inside Outer Function")
    def inner():
        return "Inside Inner Function"
        print("Inner Function")
    return "Outer Function Executed",inner()

outer()


# Example of Nested Functions - 5
# ================================

def outer(a,b):
    def inner(c,d):
        return c-d+a+b
        print("Inner Function")
    return 100,inner(10,20)

print(outer(5,15))

# Example of Nested Functions - 6
# ================================

def outer(*a):
    def inner(c,d):
        return c-d+a
        print("Inner Function")
    return 100,inner(10,20)

# print(outer(5,15))

#Example of Nested Functions -7
#================================

def outer():
    inner()
    print("Inside Outer Function")
    def inner():
        print("Inside Inner Function")
        return "Inner Executed"
    return ("Outer Function Executed")

outer()