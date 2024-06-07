#Exercise 3. Write a Python program to remove the n-th index character from a nonempty string.

string = "homeland"
n = 3
x = string[:3]
y = string[4:]
new_string = x + y
print(new_string)

#corrected

string = "homeland"
n = 3
x = string[:n]
y = string[n+1:]
new_string = x + y
print(new_string)