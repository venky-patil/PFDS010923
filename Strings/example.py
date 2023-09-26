# How to Define Multiline Characters in Strings?
# =================================================

# Example:
# ========

x = """Edyoda
    Digital
    University"""
print(x)

# Indexing Examples:
# ===================


string1 = "Good Evening I Hope Everything is Going Well"
print(string1[-5])  #""
print(string1[7]) #e
print(string1[-4]) #W
print(string1[9]) #i 
print(string1[-17])#i
print(string1[25])#t
#print(string1[100]) #Error

# Example of Positive Slicing
# =============================

string1 =  "Good Evening"
print(string1[0:12:1]) #Good Evening 
print(string1[::]) #Good Evening --> string1[0:12:1]
print(string1[2:10:3]) #oem
print(string1[4:8:3])# e 
print(string1[76:9:22])#empty string
#print(string1[::0]) #Error
print(string1[87:54:23]) #empty string
print(string1[-10:-1:2]) #o vnn
print(string1[-1:-10:5])#empty string
print(string1[-8:-2:3])#e


# Example of Negative Slicing
# =============================

string1 =  "Good Evening"
print(string1[::-1]) #gninevE doog --> string1[-1:-13:-1]
print(string1[-1:-10:-5]) #gv
print(string1[10:4:-2]) #nnv
print(string1[-4::-3])# nEo

# Example of Concatenation Operator(+):
# =================================

string1 = "Hi How are You "
string2 = "I Hope Everything is Going Well"
print(string1+string2)  # Hi How are You I Hope Everything is Going Well


# Example of Repitition Operator
# ===============================

String1 = "Hi How are You"
print(String1*5)#

# Membership Operator(in and not in):
# =====================================
string1 = "Python is a High Level Programming Language"
print("P" in string1) #True 
print("Python" in string1) #True 
print("p" in string1) #False
print("Java" not in string1) #True


# Identity Operators(is and is not):
# ===================================

string1 = "Python1"
string2 = "Python2"
string3 = "Python1"
print(string1 is string2) #False
print(string2 is string3) #False
print(string1 is not string3)#False
print(string1 is not string2)#True
print(string1 is string3)#True



# Example of Logical Operators:
# ==============================

print("Hi" and "Hello")#Hello
print("" and "How are you") #Empty 
print("Python" or "Java") #Python
print("0" or "Java") #0
print(not "") #True 
print(not "Hi") #False

# Example of Strip Function
# ===========================

string1 = "             Python is Good                       "
print(string1.strip())

# Example of Find Function
# ==========================

string1 = "Learning Python is Easy and Python is Simple"
print(string1.find("Python"))#9
print(string1.find("Python",0,15))#9 
print(string1.find("Python",15,20))#-1
print(string1.find("Java"))#-1
print(string1.find("Python"))#9
print(string1.find("python"))#-1



# Example of Index Function
# ==========================

string1 = "Learning Python is Easy and Python is Simple"
print(string1.index("Python"))#9
print(string1.index("Python",0,15))#9 
#print(string1.index("Python",15,20))#Error
#print(string1.index("Java"))#Error
print(string1.index("Python"))#9
#print(string1.index("python"))#Error


# Example of upper() Function:
# =============================

string1 = "Learning Python is Easy and Python is Simple"
print(string1.upper()) #LEARNING PYTHON IS EASY AND PYTHON IS SIMPLE


# Example of lower() Function:
# =============================

string1 = "Learning Python is Easy and Python is Simple"
print(string1.lower()) #learning python is easy and python is simple


# Example of title() Function:
# =============================

string1 = "Learning python is easy and python is simple"
print(string1.title()) #Learning Python Is Easy And Python Is Simple



# Example of capitalize() Function:
# =================================

string1 = "learning Python is easy and Python is simple"
print(string1.capitalize()) #Learning Python is easy and Python is simple


# Example of isupper() Function
# ==============================

string1 = "learning Python is easy and Python is simple"
print(string1.isupper()) #False 

# Example of islower() Function
# ==============================

string1 = "learning Python is easy and Python is simple"
print(string1.islower()) #False 

# Example of isalpha() Function
# ==============================

string1 = "learningPythoniseasyandPythonissimple"
print(string1.isalpha()) #True

string1 = "learningPythonisea9syandPythonissimple"
print(string1.isalpha()) #False



# Example of isnumeric() Function
# ==============================

string1 = "123"
print(string1.isnumeric()) #True

string1 = "123 "
print(string1.isnumeric()) #False


# Example of count() Function
# ============================

string1 = "Python is easy to Learn and Python is also a High Level Programming Language"
print(string1.count("Python"))#2 
print(string1.count("is",0,9))#1 
print(string1.count("is",9,12))#0
print(string1.count("P"))#3



# Example of Replace Function
# ============================

string1 = "Python is easy to Learn and Python is also a High Level Programming Language"
string2 = string1.replace("Python","Java")
print(string2) #Java is easy to Learn and Java is also a High Level Programming Language
string3 = string1.replace("easy","difficult")
print(string3)#Python is difficult to Learn and Python is also a High Level Programming Language

# Example of Split() Function
# ============================

string1 = "Learning Python is Easy" 

print(string1.split()) #['Learning', 'Python', 'is', 'Easy']

print(string1.split("e")) #['L', 'arning Python is Easy']

string2 = "ashu@gmail.com"
print(string2.split("@")) #["ashu","gmail.com"]

string1 = "Learning Python is Easy" 
print(string1.split("Python")) #["Learning"," is Easy"]


# Example of Join Function:
# ==========================

list1 = ["Learning","Python","is","Easy"]
print(" ".join(list1))#"Learning Python is Easy"


list1 = ["Learning","Python","is","Easy"]
print("#".join(list1))#"Learning#Python#is#Easy"

list1 = ["Learning","Python","is","Easy"]
print("99".join(list1))#"Learning99Python99is9Easy"

list1 = ["Learning","Python","is","Easy"]
print(",".join(list1))#"Learning,Python,is,Easy"


list1 = ["Learning","Python","is","Easy"]
print("".join(list1))#"LearningPythonisEasy"


# Example of input() Function
# =============================

# string1 = input("Enter a String :")
# string2 = input("Enter Second String :")
# print("Concatenation of Both the Strings is :",string1+string2)


# Example of Ord() Function 
# ===========================

print(ord("a"))#97 
print(ord("%")) #37
print(ord("0")) #48 
print(ord("#")) #35
print(ord(" ")) #32

# Example of Char() Function
# ===========================

print(chr(97))#a 
print(chr(32))# 
print(chr(35))##
print(chr(65))#A
print(chr(49))#1


# Example of Sorted Function:
# ============================

string1 = "123Ara"
print(sorted(string1))#['1','2','3','A','a','r']


string1 = "123Ara"
print(sorted(string1,reverse=True))#['r','a','A','3','2','1']


# Example of isalnum() Function 
# ================================

string1 = "124HihOWAREYOU"
print(string1.isalnum())#True 

# Example of Comparison Operator 
# ===============================

String1 = "Python"
String2 = "python"
print(String1<String2) #True
print(String1>String2) #False
print(String1==String2) #False

String3 = "PythOn"
print(String1>String3) #True
print(String2>String3) #True



