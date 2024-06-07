#3. Write a Python script that takes multiple text files as input and concatenates their
# contents into a single text file.



# name_of_files = ["Text.txt", "output.txt.txt", "input.txt.txt"]
# with open("single_text_file.txt", "w") as file:
#    for name in name_of_files:
#       with open(name) as file:
#          for line in file:
#             file.write(line)      
#             file.write("\n")
# with open("single_text_file.txt","r") as file:
#     print(file.read())

name_of_files = ["Text.txt", "output.txt.txt", "input.txt.txt"]
with open ("single_text_file.txt","w") as file:
    for name in name_of_files:
      with open (name) as file:
         for line in file:
            print(file.write(line))




