# Average Function
#Write a function that calculates the average of a list of numbers.

def find_average(numbers):
    sum = 0 
    for digit in numbers:
        sum += digit
    return sum / len(numbers)
print(find_average([1,2,3,4]))
print(find_average([5,7,8,9]))