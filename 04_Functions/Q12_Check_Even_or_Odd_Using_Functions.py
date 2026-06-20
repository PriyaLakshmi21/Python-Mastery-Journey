def even_or_odd(num):
    if num%2==0:
        return "even"
    else:
        return "odd"
num=int(input("Enter a number:"))
result=even_or_odd(num)
print("The number is:",result)
