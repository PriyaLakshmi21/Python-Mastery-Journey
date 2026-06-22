try:
    age = int(input("Enter age: "))
    if age < 0:
        print("Age cannot be negative")
    elif age < 18:
        print("Minor")
    else:
        print("Adult")
except ValueError:
    print("Please enter a valid age")