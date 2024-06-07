#1.Check Pangram Function
#Write a function that checks if a sentence is a pangram.

def ispangram(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in alphabet :
        if letter not in sentence:
            return False
    return True
print(ispangram("the quick brown fox jumps over the lazy dog"))