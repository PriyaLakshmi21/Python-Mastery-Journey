name = input("Enter Name: ")

with open("student.txt", "w") as file:
    file.write(name)

with open("student.txt", "r") as file:
    content = file.read()

print("Student Name:")
print(content)