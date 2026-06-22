num=int(input("Enter a number:"))
if num%2==0:
    print("Num is even:",num)
else:
    print("Num is Odd:",num)
if num>0:
    print("The number is positive:",num)
elif num<0:
    print("The number us Negative:",num)
else:
    print("The number is zero:",num)
print("Multiplication Table:")
for i in range(1,11):
    print(num,"x",i,"=",num*i)
sum=0
for i in range(1,num+1):
    sum+=i
print("The sum is:",sum)