try:
    num = int(input("Enter Number: "))
    result = 100 / num
    print(result)
except ValueError:
    print("Please enter a valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
      print("Program ended")