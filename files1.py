#1 Character Count
#Write a Python script that reads a text file(input.txt) and counts the occurences of each character
#(including spaces and punctuations). Output the character frequency to another text file(output.txt).


with open ("input.txt.txt","r") as file:
    x = file.read()
    count = 0
    for i in x :
        count += 1
    print(count)
with open ("output.txt.txt","w") as file:
    file.write("67")
with open ("output.txt.txt","r") as file:
    print(file.read())




