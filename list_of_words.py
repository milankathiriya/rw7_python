'''
Create a program that:
- Takes a list of words as input.
- Use list comprehension to create a new list containing only words that start with a vowel.
'''

words = []
words_vowels = []

n = int(input("Enter how many words: "))    # 5

for i in range(n):
    words.append(input("Enter word: "))

for word in words:
    # if word[0]=="a" or word[0]=="e" or word[0]=="i" or word[0]=="o" or word[0]=="u":
    if word.startswith("a") or word.startswith("e") or word.startswith("i") or word.startswith("o") or word.startswith("u"):
        words_vowels.append(word)

print(words_vowels)
