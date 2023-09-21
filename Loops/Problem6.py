#Python Program to Find To sum of Even Numbers Between a Given Range Using For Loop.

start = int(input("Enter Start Value : ")) #10
end   = int(input("Enter End Value : "))#20
sum1 = 0
for i in range(start,end+1):#10,11,12,13,14,15,16,17,18,19,20
    if i%2==0: #10,12,14,16,18,20
        sum1=sum1+i #sum1 = 0+10=10    sum1 = 10+12=22,sum1=22+14
print(sum1)

#Python Program to Find To sum of Even Numbers Between a Given Range Using While Loop.

start = int(input("Enter Start Value : ")) #10
end   = int(input("Enter End Value : "))#15
sum1 = 0
i = start
while i<end+1:
    if i%2==0:
        sum1=sum1+i
    i+=1
print(sum1) 

