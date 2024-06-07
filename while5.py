# Exercise 5. Write a Python program that calculates the Fibonacci sequence up to a given number n
# using a while loop. The Fibonacci sequence is a series of numbers where each number
# is the sum of the two preceding ones.

a, b = 0, 1
n = 5 
fibonacci_series = []
fibonacci_series.append(a) 
while b <= n:
    fibonacci_series.append(b)
    a, b = b, a + b
print(fibonacci_series)
