import json
student = {
    "name": "Priya",
    "age": 20,
    "course": "Python"
}
json_data = json.dumps(student)
print(json_data)