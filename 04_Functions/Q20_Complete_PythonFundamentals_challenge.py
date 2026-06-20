num=[]
for i in range(5):
    nums=int(input("Enter the elements:"))
    num.append(nums)
def fundamentals(num):
    largest=max(num)
    smallest=min(num)
    total=sum(num)
    average=total/len(num)
    print(num)
    print("largest=",largest)
    print("smallest=:",smallest)
    print("sum=:",total)
    print("average=:",average)
fundamentals(num)