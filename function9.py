#Write a python function which create dict from 2 lists with the same length

def dict_from_two_lists(keys,values):
    new_dict = {}
    for x in range(len(keys)):
        new_dict[keys[x]] = values[x]
    return new_dict
print(dict_from_two_lists(["Anna","Hayk"],["32","35"]))
print(dict_from_two_lists(["Mary","Narek"],["10","8"]))

