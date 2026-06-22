sentence=input("Enter a Sentence:")
with open("sentence.txt","w") as file:
    file.write(sentence)
with open("sentence.txt","r") as file:
    content=file.read()
count=len(content)
print("Total Characters=",count)