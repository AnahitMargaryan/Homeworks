# Exercise 5. Filtering Word Lenghts
# Given a list of words, create a dictionary where keys are words, and values are their lenghts, but only 
# for word with lenght greater than 3.

word_list = ["word", "flower", "sky", "sun", "people", "happines"]
myDict = {word: len(word) for word in word_list if len(word) > 3}
print(myDict)
