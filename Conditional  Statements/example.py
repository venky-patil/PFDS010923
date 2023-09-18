#Conditional Statement Example:

# x = 10
# if x==20:
#    print("x value is 10 ") 
# print("Bye")

# #Functions

# def fun():
#    print("Hi")
# print("Bye")

# #Example of if statement:

# student_name = input("Enter Your Name :")
# student_roll = input("Enter roll no :")
# if student_name=="Pratyush" and student_roll=="100":
#    print("Hello Pratyush Welcome to Edyoda...")
#    print("Hope Everything is going well...")
# print("Hello Student How are You")


# #Example of if-else Statement:

# student_name = input("Enter Your Name :")
# student_roll = input("Enter roll no :")
# if student_name=="Pratyush" and student_roll=="100":
#    print("Hello Pratyush Welcome to Edyoda...")
#    print("Hope Everything is going well...")

# else:
#    print("Sorry Please Enter Valid Student Name")
# print("Thank You")


#Example of if elif and else

# day = int(input("Enter Month Day :")) #5 --> May --> 7 --> July  8 --> August,12 --> December
# if day==1:
#     print("Januray Month it is ")
# elif day==2:
#     print("February Month it is")
# elif day==3:
#     print("March Month it is")
# elif day==4:
#     print("April Month it is")
# elif day==5:
#     print("May Month it is")
# elif day==6:
#     print("June Month it is")
# elif day==7:
#     print("July Month it is")
# elif day==8:
#     print("August Month it is")
# elif day==9:
#     print("September Month it is")
# elif day==10:
#     print("October Month it is")
# elif day==11:
#     print("November Month it is")
# elif day==12:
#     print("December Month it is")
# else:
#     print("Please Enter Valid Input")


#Example of Nested if elif and else Statement:
print("Enter D For Days and M for Month")
Choice = input("Enter Your Choice :") #X
if Choice=="M":
    month = int(input("Enter Month :"))
    if month==1:
        print("Januray Month it is ")
    elif month==2:
        print("February Month it is")
    elif month==3:
        print("March Month it is")
    elif month==4:
        print("April Month it is")
    elif month==5:
        print("May Month it is")
    elif month==6:
        print("June Month it is")
    elif month==7:
        print("July Month it is")
    elif month==8:
        print("August Month it is")
    elif month==9:
        print("September Month it is")
    elif month==10:
        print("October Month it is")
    elif month==11:
        print("November Month it is")
    elif month==12:
        print("December Month it is")
    else:
        print("Please Enter Valid Input")


elif Choice=='D':
    day = int(input("Enter Day :")) #15
    if day==1:
        print("Monday it is")
    elif day==2:
        print("Tuesday it is")
    elif day==3:
        print("Wednesday it is")
    elif day==4:
        print("Thursday it is")
    elif day==5:
        print("Friday it is")
    elif day==6:
        print("Saturday it is")
    elif day==7:
        print("Sunday it is")
    else:
        print("Please Enter Valid Day")
else:
    print("Please enter Either M or D as they are Valid inputs")

