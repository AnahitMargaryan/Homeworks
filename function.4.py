#4.  Find Index Function
#Write a function that finds the index of a given element in a list. If the element is not
# present, return -1.

def  find_index(num):
    list = [1,2,3,4,5,6,7]
    for i in list:
        if list[i] == num:
            return i
        if num not in list:
            return -1
print(find_index(3))
print(find_index(4))
print(find_index(15))

