import json
student = {
    "name": "Priya",
    "age": 20,
    "marks": 95
}
with open("student.json", "w") as file:
    json.dump(student, file, indent=4)
with open("student.json", "r") as file:
    data = json.load(file)
print(data)