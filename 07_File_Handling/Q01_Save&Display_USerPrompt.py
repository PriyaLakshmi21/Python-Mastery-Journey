with open("prompts.txt", "w") as file:
    file.write("Explain Python Functions")

with open("prompts.txt", "r") as file:
    content = file.read()

print(content)