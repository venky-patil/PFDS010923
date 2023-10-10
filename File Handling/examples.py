# # Example of write(str) Function - 1
# # ====================================

# # f = open('akshay.txt','w')
# # f.write('Vinay is a Good Boy and He knows C/C++ Programming very well')
# # f.write('Ajay')
# # f.write('Virat')
# # f.write('Rohit')
# # f.close()


# # Example of write(str) Function - 2
# # ====================================

# f = open('vinay.txt','w')
# f.write('Vinay is a Good Boy and He knows C/C++ Programming very well\n')
# f.write('Ajay\n')
# f.write('Virat\n')
# f.write('Rohit\n')
# f.close()


# # Example of write(str) Function - 3
# # ====================================

# f = open('vinay.txt','w')
# f.write('Python is a High Level Programming Langauge\n')
# f.write('Java is also high level programming langauge but syntax is little bit tricky\n')
# f.write('C/C++ is a middle level langauge\n')
# f.write('Javascript is used for web development\n')
# f.close()


# # Example of writelines(list) Function - 4
# # ==========================================

# f = open('Ashu.txt','w')
# f.writelines(['Vinay is a Good Boy and He knows C/C++ Programming very well','Ajay','Vijay','Manish','Rajeev'])
# f.close()

# # Example of writelines(list) Function - 5
# # ==========================================

# f = open('Vijay.txt','w')
# f.writelines(['Vinay is a Good Boy and He knows C/C++ Programming very well\n','Ajay\n','Vijay\n','Manish\n','Rajeev\n'])
# f.close()


# # Example of Read Operation 
# # ==========================

# # f = open('Jai.txt','r')
# # f.read()
# # f.close()


# # Example of read() Function - 1
# # =============================

# f = open('akshay.txt','r') 
# print(f.read())
# f.close()


# # Example of read(n) Function - 2
# # ================================

# f = open('akshay.txt','r') 
# print(f.read(2))
# f.close()


# # Example of read(n) Function - 3
# # ================================

# f = open('akshay.txt','r') 
# print(f.read(15))
# f.close()


# # Example of readline() Function - 4
# # ===================================

# f = open('Vijay.txt','r') 
# print(f.readline())
# f.close()

# # Example of readline() Function - 4
# # ===================================

# f = open('akshay.txt','r') 
# print(f.readline())
# f.close()


# # Example of readlines() Function - 5
# # ===================================

# f = open('Vijay.txt','r') 
# print(f.readlines())
# f.close()

# # Example of Read Operation - 1
# #=================================

# f = open('akshay.txt') #Default mode will be r mode.
# print(f.readline())
# print(f.read(3))
# print(f.readline())
# print(f.read(4))
# print(f.read())
# print(f.readlines())
# f.close()


# Example of write(str) Function - 1
# ====================================

# f = open('Vijay.txt','a')
# f.write('Vinay is a Good Boy and He knows C/C++ Programming very well')
# f.write('Ajay')
# f.write('Virat')
# f.write('Rohit')
# f.close()

# xample of write(str) Function - 2
# ====================================

# f = open('vinay.txt','a')
# f.write('Vinay is a Good Boy and He knows C/C++ Programming very well\n')
# f.write('Ajay\n')
# f.write('Virat\n')
# f.write('Rohit\n')
# f.close()


# Example of writelines(list) Function - 4
# ==========================================

# f = open('Ashu.txt','a')
# f.writelines(['Vinay is a Good Boy and He knows C/C++ Programming very well\n','Ajay\n','Vijay\n','Manish\n','Rajeev\n'])
# f.close()

# Example of r+ Mode 
# ===================

# f = open('Ashu.txt','r+')
# print(f.read())
# f.write('Hi\n')
# f.write('Hello\n')
# f.close()


# Example of w+ Mode 
# ===================

# f = open('Jai.txt','w+')
# f.write('Hi\n')
# f.write('Hello\n')
# print(f.read())
# f.close()

# Example of w+ Mode 
# ===================

# f = open('Jai.txt','w+')

# f.writelines(['Smith\n','Johnson\n','Williams\n','Brown\n','Jones\n','Miller\n','Davis\n','Garcia\n','Rodriguez\n'])
# print(f.read())
# f.close()

# Example of f.closed Attribute
# =================================

# f = open('Ajay.txt','w')
# f.write('Hi\n')
# f.write('Bye\n')
# f.write('Hello\n')
# print('Is file closed :',f.closed) #False
# f.close()
# print('Is file closed:',f.closed) #True

# Example of With Keyword 
# # =========================

# with open('Srivastava.txt','w') as f:
#     f.write('Java is high Level Programming Language\n')
#     f.write('Python is also high level programming langauge\n')
#     print('File is closed or not',f.closed) #False

# print('File is closed or not',f.closed) #True


# Example of tell Function 
# ==========================

# with open('hardik.txt','w') as f:
#     f.write('Shubhman Gill is having Dengue')
#     f.write(' So He will not able to play with Afghanisation on 11 February 2023')


# with open('hardik.txt','r') as f:
#     print(f.tell())
#     print(f.read(5))
#     print(f.tell())
#     print(f.read(10))
#     print(f.tell())


# with open('hardik.txt','r') as f:

#     print(f.read(3))
#     print(f.tell())
#     print(f.read(5))
#     print(f.tell())
#     print(f.read(20))
#     print(f.tell())



# Example of Seek(n) Function
# ==============================

# with open('hardik.txt','r') as f:
#     print(f.read(3)) #Shu
#     print(f.tell())#3
#     print(f.read(5))#bhman
#     print(f.tell())#8
#     f.seek(15)
#     print(f.tell())
#     print(f.read(5))


# with open('hardik.txt','r') as f:
#     print(f.read(10))
#     print(f.tell())
#     f.seek(20)
#     print(f.tell())
#     print(f.read(10))

# with open('hardik.txt','r') as f:
#     print(f.read(8))
#     print(f.tell())
#     f.seek(15)
#     print(f.tell())
#     print(f.read(5))

    

