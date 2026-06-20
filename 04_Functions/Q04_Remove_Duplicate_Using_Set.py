number=[]
n=int(input("Enter the number of elements:"))
for i  in range(n):
    num=int(input("Enter the numbers:"))
    number.append(num)
remove_duplicate=set(number)
print("The unique list:",remove_duplicate)