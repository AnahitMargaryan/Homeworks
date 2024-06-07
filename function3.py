#Exercise 3. Write a Python function to find the Max of three number

def max_function(num1,num2,num3):
    if num1 > num2 and num1 > num3:
           largest = num1
    elif num2 > num1 and num2 > num3:
           largest = num2
    else:
           largest = num3
    return largest
print(max_function(15,16,10))
print(max_function(19,18,21))








