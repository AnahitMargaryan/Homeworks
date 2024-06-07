# Exercise 6. Dictionary Merge
# Given two dictionaries, merge them into a new dictionary, excluding any keys that start with an underscore.

girls = {"_Ann": 18, "Mary": 22, "Susan": 23}
boys = {"_Hayk": 24, "Levon": 35, "Aram": 26}

merged = {key: value for word in (girls, boys) for key, value in word.items() if key[0] != '_'}
print(merged)
