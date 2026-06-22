try:
    num = int(input("Enter a number: "))
    square = num * num
    print("Square =", square)
except ValueError:
    print("Please enter a valid number")