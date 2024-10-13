def validarg(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()
    return sorted(word1) == sorted(word2)

word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")
print(validarg(word1, word2))