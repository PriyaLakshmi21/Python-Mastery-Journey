name = input("Enter Employee Name: ")
department = input("Enter Department: ")

with open("employee.txt", "w") as file:
    file.write("Name: " + name + "\n")
    file.write("Department: " + department)

with open("employee.txt", "r") as file:
    content = file.read()

print("Employee Details")
print(content)