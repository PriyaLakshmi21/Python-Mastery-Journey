number=int(input("Enter a number:"))
result=0
while number>0:
    remainder=number%10
    result=result*10+remainder
    number=number//10
print("reverse of number is:",result)
