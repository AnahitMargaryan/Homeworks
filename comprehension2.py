# Exercise 2. Character Frequency
# Given a string, create a dictionary where keys are characters and values are
# their frequencies in the string.

word = "comprehension"
myDict = {char: len([letter for letter in word if letter == char]) for char in word}
print(myDict)


