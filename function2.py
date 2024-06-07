#Write a Python function to calculate count of each letter in string

def characters(string):
    dict = {}
    for x in string:
        if x in dict:
            dict[x] += 1
        else:
            dict[x] = 1
    return dict
print(characters("alabama"))




