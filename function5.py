#.Write a python program which concat 2 dicts.


def contact(dict1,dict2):
    for k,v in dict2.items():
        dict1[k] = v
    return dict1
print (contact({"Aram":24,"Anna":25},{"Ani":32, "Mane": 24}))