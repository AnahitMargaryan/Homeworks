#4. Write a Python program to find intersectoin of two given arrays using Lambda.

nums_array1 = [1,3,4,5,7,8,9]
nums_array2 = [2,4,5,6,8,9]
print(list(filter(lambda x: x  in nums_array1,nums_array2)))
