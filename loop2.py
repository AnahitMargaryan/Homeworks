
# Exercise 2: Vowel Counter

sentence = "Everything you can imagine is real."
vowels = ["a","e","i","o","u"]
count = 0
for letters in sentence:
    if letters  in vowels:
        count += 1
print(count)
        