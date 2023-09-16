#Python program to Calculate Simple Interest.
Principle  =  float(input("Enter Principle Amount :"))
Rate       =  float(input("Enter Rate : "))
Time       =  float(input("Enter Time : "))

SI = (Principle*Rate*Time)/100
print("Simple Interest is ",SI)
