#1. Write a Python program to square and cube every number in a given list of integers using Lambda.

nums = (2,4,6,8,10)
print(list(map(lambda x:x**2,nums)), list(map(lambda x:x**3,nums)))