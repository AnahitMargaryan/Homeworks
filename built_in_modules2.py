# Random Password Generator
# Write a function that generates a random password for the user. Allow the user to
# specify the length and complexity of the password (include letters, numbers, and
# symbols).

import random
import string
import secrets

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation
password_content = letters + digits + special_chars

password_len = 15

password = " "
for i in range(password_len):
    password += " ".join(secrets.choice(password_content))

print(password)




