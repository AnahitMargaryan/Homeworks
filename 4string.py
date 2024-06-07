#Exercise 4. Write a Python program to change a given string to a new string where the first and last chars
#have been exchanged

string = "beautiful"
first_char = string[0]
middle_chars = string[1:-1]
last_cahr = string[-1]
new_string = last_cahr + middle_chars + first_char
print(new_string)
