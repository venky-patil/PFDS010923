#Python Program to Check weather a Given Number is Divisble by 3 and 5 and 9 or Not.

#Variations-1 

# if number%3==0 and number%5==0 and number%9==0:
#     print("Number is Completely divisble by 3,5 and 9")
# else:
#     print("Number is not Divisble by 3,5 and 9 ")

#Variation-2:

number = int(input("Enter a Number :")) #30
if number%3==0:
    if number%5==0:
        if number%9==0:
            print("Number is Completely divisble by 3,5 and 9")
        else:
            print("Number is divisble by 3 and 5 but not 9 ")
    else:
        print("Number is divisble by 3 but not 5 ")
else:
    print("Number is not divisble by 3")




