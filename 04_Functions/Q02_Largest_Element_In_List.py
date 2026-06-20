numbers = []
n = int(input("How many numbers do you want to enter? "))
for i in range(n):
    num = int(input("Enter a number: "))
    numbers.append(num)
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print("Largest Number =", largest)
# numbers=[10,20,50,800,150]
# largest=max(numbers)
# print(largest)