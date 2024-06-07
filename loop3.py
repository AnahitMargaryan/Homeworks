# Exercise 3: Word Finder
        
word_list  = ["alarm","armstace","notebook","harmful","sky"]
target_word = "arm"
final = []
for words in word_list:
    if target_word in words:
        final.append(words)
        print(words)