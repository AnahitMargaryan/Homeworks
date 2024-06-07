#Exercise 1. Write a Python function to sum all the numbers in a list:(8,2,3,0,7)


def list_sum(sequence):
    sum = 0
    for i in sequence:
        sum = sum + i
    return sum
print(list_sum([8,2,3,0,7]))




