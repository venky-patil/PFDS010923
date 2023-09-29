# Example of Creation of Set Objects 
# ===================================

set1 = {}
print(type(set1)) #<class dict>

set2 = set()
print(type(set2))#<class set>

set3 = {10,20,30}
print(type(set3))#<class set>

# Example of Add() Function 
# ==========================

set1 = set()
set1.add(10)
set1.add("Hi")
set1.add(10.5)
print(set1)

# Example of Update Function 
# =============================

set1 = {10,20,30,40,50}
list1 = [10,20,80,90,60]
set1.update(list1)
print(set1)#{80, 50, 20, 90, 40, 10, 60, 30}
set1.update(("Hi","Hello"))
print(set1)#{'Hi', 10, 80, 20, 'Hello', 90, 30, 40, 50, 60}

# Example of Pop() Function 
# ==========================

set1 = {'Hi', 10, 80, 20, 'Hello', 90, 30, 40, 50, 60}
print(set1.pop())#40
print(set1)#{10, 'Hello', 'Hi', 80, 50, 20, 90, 60, 30}

# Example of Remove Function 
# ============================
set1 = {'Hi', 10, 80, 20, 'Hello', 90, 30, 40, 50, 60}
set1.remove("Hello")
print(set1)
# set1.remove("Python")# Key Error
# print(set1)

# Example of Discard Function 
# ============================

set1 = {'Hi', 10, 80, 20, 'Hello', 90, 30, 40, 50, 60}
set1.discard("Hello")
print(set1)
set1.discard("Python")
print(set1)


# Example of Intersection Function 
# ===================================
s1 = {10,20,30,40,50,60}
s2 = {70,80,90,100,10,20}
s3 = {"Java","Python"}
print(s1.intersection(s2))#{10,20}
print(s1.intersection(s3))#set() 


# Example of Union Function 
# ==========================

s1 = {10,20,30,40,50,60}
s2 = {70,80,90,100,10,20}
s3 = {"Java","Python"}
print(s1,s2,s3)
print(s1.union(s2))#{10,20,30,40,50,60,70,80,90,100}
print(s1.union(s3))#{10,20,30,40,50,60,"Java","Python"}

# Example of Difference Function 
# ===============================

s1 = {10,20,30,40,50,60}
s2 = {70,80,90,100,10,20}
print(s1.difference(s2))#{30,40,50,60}
print(s2.difference(s1))#{70,80,90,100}
