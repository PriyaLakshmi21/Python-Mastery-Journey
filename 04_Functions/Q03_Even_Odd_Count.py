numbers=[]
n=int(input("enter the number of elements:"))
ecount=0
ocount=0
for i in range(n):
    num=int(input("Enter the numbers:"))
    numbers.append(num)
for num in numbers:
    if num%2==0:
        ecount+=1
    else:
        ocount+=1
print("Even Count is:",ecount)
print("Odd Count is:",ocount)