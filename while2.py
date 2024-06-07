# Write a Python program that asks the user to enter a password. Keep asking for the
# password until the correct password "secret" is entered. Provide appropriate feedback
# to the user.

password= input("What is the password?")
correct_password= 'Secret'

while password != correct_password:
    password = input ("Enter password again")
print ("Success")