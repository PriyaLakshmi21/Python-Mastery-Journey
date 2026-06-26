sentence = input("Enter a sentence: ")
with open("sentence.txt", "w") as file:
    file.write(sentence)
with open("sentence.txt", "r") as file:
    content = file.read()
words = content.split()
print("Total Words =", len(words))