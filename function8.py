# Write a python function, which create a dictionary for given number N, where keys are numbers from
# 1 to N, and values are cubs of that numbers.

def create_dictionary(digits):
    dict = {"digits":0}
    for num in digits:
        dict[num] = num ** 3
    return dict
print(create_dictionary(range(1,15)))