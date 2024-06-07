#5. Sum of Squares Function
#Write a function that calculates the sum of squares of numbers from 1 to n.

def sum_of_squares(n):
    sum = 0
    for digit in range(1, n+1):
        sum = sum + (digit ** 2)
    return sum
print(sum_of_squares(5))
print(sum_of_squares(10))