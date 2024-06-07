#Exercise 1. Arrange string characters such that lowercase letters should come first.

word = "HomELanD"
lowers = []
uppers = []
for letter in word:
    if letter.islower():
        lowers.append(letter)
    elif letter.isupper():
            uppers.append(letter)
print( "".join(lowers + uppers))



    
   

