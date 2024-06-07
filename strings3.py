#Exercise 3. Write a program to check if two strings are balanced. For example, strings s1 and
#s2 are balanced if all the characters in the s1 are present in s2. The character’s
#position doesn’t matter.

#example 1

word1 = "odlw"
word2 = "wonderful" 
balanced = "True"
for chars in word1:
    if chars in word2: 
        continue
    else:
        balanced = "False" 
print(balanced)

#example 2

string1 = "sthj"
string2 = "strawberry"
balanced_word = "True"
for letters in string1:
    if letters in string2:
        continue
    else:
        balanced_word = "False"
print(balanced_word)
      

