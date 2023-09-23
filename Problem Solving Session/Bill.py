Unit = float(input("Enter Meter Unit : "))
Price = 0
if Unit>0 and Unit<100:
    Price = 0 
    print("The Electricity Bill is ",Unit)

elif Unit>100 and Unit<200:
    Price = 5
    print("The Electricity Bill is ",Price*Unit)

elif Unit>200:
    Price = 10 
    print("The Electricity Bill is ",Unit*Price)