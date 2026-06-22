marks = []
for i in range(5):
    mark = input("Enter mark: ")
    marks.append(mark)
with open("marks.txt", "w") as file:
    for mark in marks:
        file.write(mark + "\n")
with open("marks.txt", "r") as file:
    content = file.read()
print(content)