
sentence = input("Enter a sentence: ")
words = sentence.split()
max_length = 0
longest_word = ""
for word in words:
    if len(word) > max_length:
        max_length = len(word)
        longest_word = word
print("Longest Word =", longest_word)