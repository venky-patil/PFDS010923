# # Example of Math Module 
# # =======================

# import math 
# #print(help(math))
# print(math.factorial(5))#120
# print(math.sqrt(144))#12
# print(math.sin(200))
# print(math.tanh(200))
# print(math.ceil(5.4))#6
# print(math.floor(6.5))#6
# print(math.pi)
# print(math.e)
# print(math.tau)

# # Example of random.random()
# # =============================

# import random
# print(random.random()) #

# # Generate 10 random Numbers between 0 to 1
# # ===========================================

# for i in range(10):
#     print(random.random())

# # Example of random.randint()
# # =============================

# import random
# print(random.randint(10,100))

# #Generate 10 random Numbers between 999 to 9999
# #=============================================

# for i in range(10):
#     print(random.randint(1000,9999))


# # Example of random.uniform()
# # =============================

# import random
# print(random.uniform(5,10))


# # Generate 10 random Numbers between 999 to 9999 in form of Floating Point  Number 
# # ======================================================================================

# for i in range(10):
#     print(random.uniform(999,9999))


# # Example of User Defined Module 
# # ===================================

# import calculator
# #print(help(calculator))
# print(calculator.add(10,20))
# print(calculator.subtraction(10,20))
# print(calculator.multiplication(10,20))
# print(calculator.division(10,20))
# print(calculator.floor_division(10,20))
# print(calculator.name)
# print(calculator.college)



# # Example of Packages-1
# # ======================

# import python.sub 
# import python.add
# #print(help(python.sub))
# print(python.sub.subtraction(10,20))
# print(python.add.addition(10,20))



# # Example of Packages-2
# # ======================

# import packagedemo.armstrong
# #print(help(packagedemo.armstrong))
# num = int(input("Enter a number :"))
# n = packagedemo.armstrong.armstrong(num)
# if n:
#     print("Number is Armstrong Number")
# else:
#     print("Number is not Armstrong")



# # Example of Packages-3
# # ======================

# # import packagedemo.strong
# # #print(help(packagedemo.strong))
# # num = int(input("Enter a number :"))
# # n = packagedemo.strong.strong(num)
# # if n:
# #     print("Number is Armstrong Number")
# # else:
# #     print("Number is not Armstrong")


# # Example of Modules/Packages with From Keyword -1 
# # ====================================================

# from math import factorial,sqrt  #Only Two Functions from math module will be imported.

# print(factorial(10))
# print(sqrt(144))
# #print(floor(6.5)) #Error


# # Example of Modules/Packages with From Keyword -2
# # ====================================================

# from math import *  #Whatever variables/classes/functions are available in that module will be imported in your current file.

# print(factorial(10))
# print(sqrt(144))
# print(floor(6.5))
# print(pi)
# print(e)

# # Example of Modules/Packages with From Keyword -3
# # ====================================================

# from calculator import *  #Whatever variables/classes/functions are available in that module will be imported in your current file.

# print(add(10,20))
# print(subtraction(10,20))
# print(multiplication(10,20))
# print(division(10,20))



# # Example of Modules/Packages with From Keyword -4
# # ====================================================

# from calculator import add,subtraction,multiplication 

# print(add(10,20))
# print(subtraction(10,20))
# print(multiplication(10,20))
# print(division(10,20))


# Example of Modules/Packages with From Keyword -5
# ====================================================

# from packagedemo.strong import *
# from packagedemo.armstrong import *
# from python.add import *
# print(strong(145))
# print(armstrong(153))
# print(addition(10,29))


# Example of Module Aliasing.
# ===========================

import random as r 
import math as m
import calculator as nik

print("Random Number Generated",r.randint(10,20))
print(r.uniform(1,100))
print("Factorail Value is :",m.factorial(10))
print("Addition is :",nik.add(10,20))









