marks=[]
n=int(input("Enter the number of elements:"))
for i in range(n):
    mark=int(input("Enter the numbers:"))
    marks.append(mark)
total=sum(marks)
average=total/n
print("The average marks is:",average)