# Example of List Creation 
# ==========================

list1 = []
print(type(list1))
list2 = list()
print(type(list2))
list3 = [10,20,30,40,50]
print(type(list3))


# Example of Indexing in Python:
# ==============================


list1 =[10,20,30,40,50,60,70]
print(list1[-5])  #30
#print(list1[7]) #Error
print(list1[-4]) #40
# print(list1[9]) #Error 
# print(list1[-17])#Error
# print(list1[25])#Error
# print(list1[100]) #Error
print(list1[-1])#70



# Example of Positive Slicing
# =============================


list1 =  ["Learning","Python","is","Easy","and","Simple"]

print(list1[0:6:1])  #["Learning","Python","is","Easy","and","Simple"]
print(list1[::]) #["Learning","Python","is","Easy","and","Simple"]
print(list1[2:10:3])#['is','simple']
print(list1[4:8:3])# ['and']
print(list1[76:9:22])#[]
#print(list1[::0]) #Error
print(list1[87:54:23]) #[]
print(list1[-10:-1:2])#["Learning","is","and"]
print(list1[-1:-10:5])#[]
print(list1[-8:-2:3])#["Learning","Easy"]


# Example of Negative Slicing
# =============================

list1 =  ["Learning","Python","is","Easy","and","Simple"]
print(list1[::-1]) #['Simple', 'and', 'Easy', 'is', 'Python', 'Learning']
print(list1[-1:-10:-5]) #['Simple','Learning']
print(list1[10:4:-2]) #['Simple']
print(list1[-4::-3])#['is']
print(list1[-1:-4:-5]) #['Simple']
print(list1[-100:-2:-2])#[]
#print(list1[-20:-2:0])#Error
print(list1[-9:-1:-5])#[]
print(list1[:-1:-2])#
print(list1[-99:-10:-3])#[]
print(list1[-3:-99:-2])#['Easy','Python']
print(list1[:-1:-2])#[]
print(list1[-2:-1:-2])#[]
print(list1[-2:-2:-2])#[]
print(list1[-3:-2:-1])#[]
print(list1[-5:-3:-1])#[]
print(list1[-3:-5:-1])#["Easy","is"]
print(list1[-400:-5:-1])#[]

# Example of Count() Function
# ============================

list1 = [10,20,30,10,20,30,40,10,20,40,304,40]
print(list1.count(10))#3
print(list1.count(40))#3
print(list1.count(304))#1 
print(list1.count(1000))#0


# Example of Index() Function 
# ============================

list1 = [10,20,30,10,30,40,"Hello","World"]
print(list1.index("Hello"))#6
print(list1.index(40))#5 
print(list1.index(30))#2 
#print(list1.index(100))#Value Error


# Example of reverse Function()
# ==============================

list1 = [10,20,30,40,50,70]
list1.reverse()
print(list1) #[70,50,40,30,20,10]



# Example of Append() Function 
# =============================

list1 = []
list1.append("Python") #["Python"]
list1.append("Java") #["Python","Java"]
list1.append("C++") #["Python","Java","C++"]
list1.append("JavaScript") #["Python","Java","C++","JavaScript"]
list1.append(" ")
list1.append(" ")
list1.append(10)
list1.append(10.5)
list1.append(True)
list1.append(10+20j)
list1.append([10,20,30])
print(list1)


# Example of insert() Function 
# =============================

list1 = [10,20,30,40,50,60]
list1.insert(1,2000)#[10,2000,20,30,40,50,60]
list1.insert(0,1000)#[1000,10,2000,20,30,40,50,60]
list1.insert(100,300)#[1000,10,2000,20,30,40,50,60,300]
list1.insert(-200,400)#[400,1000,10,2000,20,30,40,50,60,300]
print(list1)#[400,1000,10,2000,20,30,40,50,60,300]


# Example of Extend Function 
# ===========================

list1 = [10,20,30,40,50]
list2 = [90,80,70]
list3 = {10:"Hi",20:30,30:40,70:50,80:50}
list1.extend(list2)
print(list1)#[10,20,30,40,50,90,80,70]
list2.extend(list3)
print(list2)


# Example of Pop Function Without Argument 
# ==========================================

list1 = ['Simple', 'and', 'Easy', 'is', 'Python', 'Learning']

print(list1)#['Simple', 'and', 'Easy', 'is', 'Python']

list2 = []
#print(list2.pop()) #Error



# Example of Pop Function Without Argument 
# ==========================================

list1 = ['Simple', 'and', 'Easy', 'is', 'Python', 'Learning']
print(list1.pop(2))#'Easy'
print(list1)#['Simple', 'and',  'is', 'Python','Learning']


list3 = ['Simple', 'and', 'Easy', 'is', 'Python', 'Learning']
#print(list3.pop(200))#Error
print(list1)#['Simple', 'and',  'is', 'Python','Learning']

list2 = []
#print(list2.pop()) #Error



# Example of Remove Function 
# ===========================

list1 = [10,20,30,40,50,60]
list1.remove(10)
print(list1)#[20,30,40,50,60]


# list2 = [10,20,30,40]
# list2.remove(100) #Error

list2 = [10,20,30,40,10,20,30]
list2.remove(20) 
print(list2)

# Example of Sorted Function 
# ==========================

list1 = [98,23,84,23,124,573,1837]
print(sorted(list1))#[23, 23, 84, 98, 124, 573, 1837]
print(sorted(list1,reverse=True)) #[1837, 573, 124, 98, 84, 23, 23]

list2 = ["Java","Python","10.5"]
print(sorted(list2))#["10.5","Java","Python"]


# list2 = ["Java",10,"10.5",20.88]
# print(sorted(list2))#Error

# Example of Concatenation Operator(+):
# =====================================

list1 = [10,20,30,40,50]
list2 = [60,70,80,90,100]
print(list1+list2)  # [10,20,30,40,50,60,70,80,90,100]



# Example of Repitition Operator
# ===============================

list1 = [10,20,30]
print(list1*3)#[10,20,30,10,20,30,10,20,30]

# Membership Operator(in and not in):
# =====================================

list1 = [10,20,30,"Java","Python","C","C++"]
print(10 in list1) #True 
print("Python" in list1) #True 
print("C" in list1) #True
print("Java" not in list1) #False


# Identity Operators(is and is not):
# ===================================

list1 = [10,20,30]
list2 = [40,50,60]
list3 = [10,20,30]
print(list1 is list2) #False
print(list2 is list3) #False
print(list1 is not list3)#True
print(list1 is not list2)#True
print(list1 is list3)#False


# Example of Logical Operators:
# ==============================

print([] and [10,20,30])#[]
print([10,20,30] and []) #[]
print([10,20,30] and [10])#[10]
print([10,20] or []) #[10,20]
print([] or [10]) #[10]
print(not []) #True 
print(not [10,20,30]) #False


# Example of Comparison Operator 
# ===============================

list1 = [10,20,30,40,50]
list2 = [40,50,60,70,80]
list3 = ["Java","Python"]
print(list1<list2) #True
print(list1>list2)#False
# print(list1>list3) #Error



# List vs Mutability
# ===================

# Example:
# ========

list1 = [10,20,30,40,50]
print(list1,id(list1))
list1.append("Java")
list1.append("C++")
list1.append("Python")
print(list1,id(list1))

# Traversal Over a List 
# ========================

# 1st Way
# =======
# By Using Len Function along with range Function(Index Value) 
# ==============================================================

list1 = ["Java","Python","C++","JavasScript","C","R"]

for i in range(len(list1)):
    print(list1[i])


# 2nd Way
# =======
# By Using Direct List Datatype
# ==============================================================

list1 = ["Java","Python","C++","JavasScript","C","R"]

for i in list1:
    print(i)

#How to take list as an input 
#=================================

# By Using For loop 
# ===================

# num = int(input("Enter the Number of Elements of the List : "))
# list1 = []
# for i in range(num):
#     ele = int(input("Enter Elements : "))
#     list1.append(ele)
# print(list1)

# Sort Vs sorted
# ===============

# Explaination
# ==============

list1 = [98,34,42,13,53,1452,12,56]
print(list1)
print(id(list1))
print(id(sorted(list1)))
print(list1)


list1 = [98,34,42,13,53,1452,12,56]
print(list1)
print(id(list1))
list1.sort()
print(list1)

# How to Change the Element of List 
# ===================================

list1 = [10,20,30,40,50]
print(id(list1))
list1[1] = 5000
print(id(list1))
print(list1)