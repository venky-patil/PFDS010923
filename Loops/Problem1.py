#Python Program to Print Even Numbers  Between 10 and 20.

#First Way:

for i in range(10,21): #10 11 12 13 14 15 16 17 18 19 20
    if i%2==0:
        print(i)


#Second Way
for i in range(10,21,2): #10,12,14,16,18,20

    print(i)

#Third Way 
list1 = list(range(10,21,2))
print(list1)

