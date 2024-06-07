#2. Find and Replace
#Implement a Python program that reads a text file (input.txt), promts the user for a word to find, and another word to replace it with.
#Replace all occurrences of the first word with the second word  and save the modified text to a new file(output.txt).

search_text = "bbb"
replace_text = "kkk"
with open ("Text.txt","r") as file:
    x = file.read()
    modified_text = x.replace(search_text,replace_text)
with open("output.txt","w") as file:
    print(file.write(modified_text))
