# Exercise 4. Character ASCII Values
# Given a string, create a dictionary where keys are characters, and values are their ASCII values.

word = "language"
myDict = {letter: ord(letter) for letter in word}
print(myDict)