#1.Write a python function, which add a new value with given key in dict.

def add_to_dict(dictionary, key, value):
    
     dictionary[key] = value

my_dict = {'a': 1, 'b': 2}
print(my_dict)

add_to_dict(my_dict, 'c', 3)
print( my_dict)
