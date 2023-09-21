# # Example: Generate Number From 0 to 9 
# # ======================================

# # First Way:
# # ==========
# num = list(range(9)) #first_argument = 0 , Second_argument = 9 , third_argument = 1
# print(num)

# # Example 2: Generate Numbers From 10 to 100
# # ===========================================

# # First Way:
# # ===========

# num = list(range(10,100)) #10 to 99
# print(num)

# # Second Way:
# # ===========

# num = list(range(10,100,1)) #10 to 99
# print(num)

# # Python Program to Print each and every Element of  List.
# # ==============================================================

# list1 = [10,20,30,40,50,60]
# for i in list1:
#     print(i)


# # Python Program to Print each and every Character of a String.
# # ==============================================================

# string1 = "Edyoda"
# for i in string1:
#     print(i)  

# # Python Program to Print Numbers from 0 to 9:
# # ==============================================

# for i in range(0,10): #0 1 2 3 4 5 6 7 8 9
#     print(i) 

# for i in range(3):
#     for j in range(3):
#         print("I value is : ",i,"J Value is",j)

# for i in range(2): #0,1
#     for j in range(3): #0,1,2
#         print(i,j)


# # Example:
# # =========
# # Python Program to Print Hello World 5 Times:
# # ===============================================
# i = 0
# while i<5:
#     print("Hello World")
#     i=i+1

# # Example of Break Keyword:
# # ===========================
# for i in range(10): #0,1,2,3,4,5,6,7,8,9
#     if i==5:   #0   ,     1         2       3      4       
#         break
#     print(i)


# # Example of Continue Statements:
# # =================================

# cart = [100,200,200,300,40005,60004,5006,46000]
# for i in cart:
#     if i>=300:
#         continue 
#     print(i)

# for i in range(10): #0,1,2,3,4,5,6,7,8,9
#     if i==3:
#        print("Continue Encounted SKip this iteration")
#        continue 
#     print(i)

# # Example of break statement with NESTED LOOP:

# for i in range(3): #0,1,2
#     for j in range(3):  #0,1,2
#         if j==1:
#            break 
#         print(i,j)  #0,0

# for i in range(4): #0,1,2,3
#     for j in range(2): #0,1
#         print(i,j)

# for i in range(4): #0,1,2,3
#     for j in range(2): #0,1
#         if j==0:        
#            break 
#         print("hello")


for i in range(3):#0,1,2
    for j in range(3):  #0,1,2
        if j==1:
            continue 
        print(i,j)
x=10
if x==10:
    pass

for i in range(1,10):
    pass

i=0
while i<5:
    print("hi")
    i=i+1
    pass