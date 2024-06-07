#6. Count Words Function
# Write a function that counts the number of words in a sentence.

def count_words(sentence):
    words = len(sentence.split())
    return words
print(count_words("The Sun will rise again."))
