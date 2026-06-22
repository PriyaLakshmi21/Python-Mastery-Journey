feedback=input("Enter Your Feedback Here:")
with open("feedback.txt","w") as file:
    file.write(feedback)
with open("feedback.txt","r") as file:
    content=file.read()
print(content)
