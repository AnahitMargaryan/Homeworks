
#Exercise 5. Write a Python program to remove duplicates from a list.

numbers = [10,25,63,25,89,45,10,56]
final_digits = []
for digits in numbers:
    if digits not in final_digits:
        final_digits.append(digits)
print(final_digits)
