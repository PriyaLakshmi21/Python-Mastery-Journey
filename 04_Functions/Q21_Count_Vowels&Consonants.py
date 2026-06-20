word=input("Enter a word:")
vowel_count=0
consonant_count=0
for char in word:
    if char in "aeiouAEIOU":
      vowel_count+=1
    else:
       consonant_count+=1
print("Vowels count=:",vowel_count)
print("Consonants count=:",consonant_count)