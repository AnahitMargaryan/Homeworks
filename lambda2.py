#2. Write a Python program to find if a given string starts with a given character using Lambda.

check = lambda string, char: string.startswith(char)
given_string = "hello world"
given_char = "h"
if check(given_string, given_char):
    print(f"The string '{given_string}' starts with the character '{given_char}'.")
else:
    print(f"The string '{given_string}' does not start with the character '{given_char}'.")
