#5. Write a Python program to add two given lists using map and lambda.

nums1 = (5,7,9,12)
nums2 = (7,6,14,9)
print(list(map(lambda x,y: x + y, nums1, nums2)))