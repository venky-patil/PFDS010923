#How can i get All keywords of Python?
import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))

#Immutability Check for Integer Datatype

number = 10
print(id(number))#2465393738256
number = number+20
print(id(number)) #2465393738896


#Immutability Check for float Datatype

number = 10.5
print(id(number))#2463768748304
number = number+20.5
print(id(number)) #2463768748464


#Immutability Check for String Datatype

number = "Hi"
print(id(number))#2168630554800
number = number+"How Are You"
print(id(number)) #2168630879792


#Immutability Check for Boolean Datatype

number = True
print(id(number))#140723151821672
number = number+True
print(id(number)) #2788678369552

#Immutability Check for Complex Datatype

number = 10+20j
print(id(number))#2556265734128
number = number+1+2j
print(id(number)) #2556265734480

#Immutability Check for Tuple Datatype

# number = (10,20,30)
# print(id(number))#1282724666880
# number[1] = 200  #Error



#Mutability check for List Object

number = [10,20,30,40,50]
print(id(number))#
number[2] = 2000  
print(id(number))


#Keys cannot of Mutable Type

x = {[10,20,30]:40,10:30,40:50}
print(x) #Error