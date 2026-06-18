num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
num3=int(input("Enter third number:"))
if (num1>num2) and (num1>num3):
    print("Num1 is greater",num1)
elif (num2>num1) and (num2>num3):
    print("Num2 is greater:",num2)
else:
    print("Num3 is greater:",num3)