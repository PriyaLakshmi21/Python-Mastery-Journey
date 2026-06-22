evenCount=0
oddCount=0
for i in range(10):
    num=int(input("Enter number:"))
    if num%2==0:
      evenCount+=1
    else:
      oddCount+=1
print("Even Count is:",evenCount)
print("Odd Count is:",oddCount)