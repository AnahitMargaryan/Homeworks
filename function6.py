#3Write a Python function to return the even numbers from a given list:[1,2,3,4,5,6,7,8,9]

def even_funct(numbers):
    final = []
    for x in numbers:
        if x % 2 == 0:
            final.append(x)
    return final
print(even_funct([1,2,3,4,5,6,7,8,9]))
print(even_funct([1,5,9,6,4,7,12,36]))