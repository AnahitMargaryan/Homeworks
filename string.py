#Exercise 1. Write a Python program to get a string made of the first 2 and the last 2 chars from a given string.

string = "wonderful"
first_chars = string[:2]
last_chars = string[-2:]
new_string = first_chars + last_chars
print(new_string)