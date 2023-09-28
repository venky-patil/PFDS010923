# Example of Creation of Tuple
# ==============================

num = (10,20,30)
print(type(num))#<class tuple>

num = tuple()
print(type(num))#<class tuple> 

num = (10,)
print(type(num))#<class tuple> 

num = (10)
print(type(num))#<class int>

num = ("Hello")
print(type(num))#<class string>

# Example of Tuple Packing:
# ==========================

num = 10,20,"Hi","Hello",10.5
print(num)
print(type(num))



# Tuple UnPacking 
# ===============

x,y,z = 10,20,30
print(x)# 10,20,30 

# x,y = 10,20,30 
# print(x,y)#Error

# Example of Indexing in Python:
# ==============================

tuple1 = (10,20,30,40,"Java","Python")
print(tuple1[-5])#20
print(tuple1[3])#40
print(tuple1[5])#'Python'
print(tuple1[0])#10
# print(tuple1[-100])#Error
# print(tuple1[50])#Error


# Example of Positive Slicing
# =============================

tuple1 = (10,20,30,40,"Java","Python")
print(tuple1[10:20:2])#Empty Tuple
print(tuple1[5:8:2])#('Python',)
print(tuple1[2:5:3])#(30,)
print(tuple1[::])#(10,20,30,40,"Java","Python")
print(tuple1[-5:-1:2])#(20,40)
print(tuple1[-100:-200:2])#Empty Tuple 
#print(tuple1[0:0:0])#Error


# Example of Negative Slicing
# =============================

tuple1 = (10,20,30,40,"Java","Python")
print(tuple1[::-1])#('Python','Java',40,30,20,10)
print(tuple1[-1:-5:-2])#('Python',40)
print(tuple1[-100:-2:-1])#Empty Tuple
print(tuple1[-2:-100:-2])#('Java',30,10)
print(tuple1[10:-5:-2])#('Python',40)
print(tuple1[100:-6:-3])#('Python',30)
# print(tuple1[:-1:0])#Error



# Example of Concatenation Operator(+):
# =====================================

tuple1 = (10,20,30,40,50)
tuple2 = (60,70,80,90,100)
print(tuple1+tuple2)  # (10,20,30,40,50,60,70,80,90,100)

# Example of Repitition Operator
# ===============================

tuple1 = (10,20,30)
print(tuple1*5)#(10,20,30,10,20,30,10,20,30,10,20,30,10,20,30)



# Membership Operator(in and not in):
# =====================================

tuple1 = (10,20,30,"Java","Python","C","C++")
print(10 in tuple1) #True 
print("Python" in tuple1) #True 
print("C" in tuple1) #True
print("Java" not in tuple1) #False


# Identity Operators(is and is not):
# ===================================

tuple1 = (10,20,30)
tuple2 = (40,50,60)
tuple3 = (10,20,30)
print(tuple1 is tuple2) #False
print(tuple2 is tuple3) #False
print(tuple1 is not tuple3)#False
print(tuple1 is not tuple2)#True
print(tuple1 is tuple3)#True



# Example of Logical Operators:
# ==============================

print(() and (10,20,30))#()
print((10,20,30) and ()) #()
print((10,20,30) and (10))#10
print((10,20) or ()) #(10,20)
print(() or (10)) #(10)
print(not ()) #True 
print(not (10,20,30)) #False


# Example of Comparison Operator 
# ===============================

tuple1 = (10,20,30,40,50)
tuple2 = (40,50,60,70,80)
tuple3 = (10,"Python")
print(tuple1<tuple2) #True
print(tuple1>tuple2)#False
#print(tuple1>tuple3) #Error


# Example of Immutability in Tuple:
# ===================================

tuple1 = (10,20,30,40,50,60)
tuple1[3] = 500 #Error
print(tuple1)