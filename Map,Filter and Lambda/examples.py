# By Using User Defined Function 
# ================================

def square(n):
    return n**2

print(square(5)) #25


# By Using Lambda Function 
# ===========================

# variable_name =  lambda parameter : expression

squared = lambda n : n**2

print(squared(7))


# Python Program to Add Two Number
# =================================

# By Using User Defined Function 
# ===============================

def add(x,y):
    return x+y 

print(add(10,20))

# By Using Lambda Function 
# =========================

# variable_name =  lambda parameter : expression

sums = lambda x,y : x+y
print(sums(100,200))


# Python Program to Find the Maximum of Two Numbers 
# ==================================================

# By Using User Defined Function 
# ===============================

def maximum(a,b):
    if a>b:
        return "First Number is Greater"
    else:
        return "Second Number is Greater"

print(maximum(10,20))


# By Using Lambda Function 
# ==========================


# variable_name =  lambda parameter : expression

maxi = lambda a,b : "First Number is Greater" if a>b  else "Second Number is Greater"
print(maxi(10,20))

# Python Program to Find Weather a Given Number is Odd or Even. 
# ==============================================================

# By Using Lambda Function 
# =========================

# variable_name =  lambda parameter : expression

odd_even = lambda n : "n is even" if n%2==0 else "n is odd"

print(odd_even(10))



# Python Program to Find Maximum of Three Numbers 
# =================================================

# By Using Lambda Function 
# ==========================

# variable_name = lambda parameter : expression

maximum_three = lambda a,b,c : "a is Greater" if a>b and a>c  else "b is greater" if b>c else "c is greater"
print(maximum_three(10,1,2))





# Example of Filter Function 
# ===========================

# Without Lambda and Filter 
# ===========================

def odd_even(n):
    if n%2==0:
        return True
    else:
        return False

l1 = [99,23,12,78,55,79,25]

num = list(filter(odd_even,l1))
print(num)

# With Lambda and Filter 
# ========================

l1 = [99,23,12,78,55,79,25]

num = list(filter(lambda n : True if n%2==0 else False,l1))
print(num)



# Example of Filter Function -2
# ==============================


# With Lambda and Filter 
# ======================

cart = [100,200,500,700,800,900,1000,1200,1400,2000]

# Filter out all the prices from the cart which is greater 1000.

filter_values = list(filter(lambda n: True if n>1000 else False,cart ))
print(filter_values)



# Example of Filter Function -2
# ==============================


# With Lambda and Filter 
# ======================

#Filter out Numbers  from 1 to 500 which are divisble by 7 and 9.

div = list(filter(lambda x:True if x%7==0 and x%9==0 else False,range(1,501)))
print(div)


# Example of Map Function 
# ========================

# Without Lambda  and Map 
# =========================

l1 = [2,4,5,6,7,19,10]

#Square of Each and Every Element of the list. 

def double(l1):
    l2 = []
    for i in l1:
       l2.append(i**2)
    return l2

print(double(l1))

# With Lambda But No Map  
# =======================

l1 = [2,4,5,6,7,19,10]

def double_n(l1):
    l2 = []
    for x in l1:
        temp = lambda x:x**2 
        l2.append(temp(x))
    return l2

print(double_n(l1))


# Without Lambda and Map Function 
# ================================

def double(n):
    return n**2

l1 = [2,4,5,6,7,19,10]

l = list(map(double,l1))
print(l)


# With Lambda and Map Function 
# ==============================

l = list(map(lambda n:n**2,l1))
print(l)


# Example of MAP Function -2
# ===========================
 
l1 = [2,4,5,6,7,19,10]
l = list(map(lambda x:True if x%2==0 else False,l1))
print(l)

# By Using Map Function(List Input) 
# =====================================

a = list(map(int,input().split()))
print(a)
print(type(a))

# Example of Reduce Function 
# ============================

from functools import reduce
l = [10,20,30,40,50] 
result = reduce(lambda x,y:x+y,l)
print(result)


from functools import reduce
l = [10,20,30,40,50] 
result = reduce(lambda x,y:x*y,l)
print(result)


# Example of Function Aliasing 
# =============================

def wish(name):
    print("Good Evening ",name)
    return ""

greeting = wish
wish("Ansh")
greeting("Aryan")

del wish
greeting('Pratyush')


# Example of String Formatting 
# ===============================
i=1
print("This is my i")
print(f"This is my {i}")


# Example of String Formatting 
# ===============================
l  = [10,20,30,40,50,60]
for i in range(len(l)):
    print(f"{l[i]} is Present at index {i}")

