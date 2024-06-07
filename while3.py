# Write a Python program that calculates the sum of all even numbers between 1 and 100
# using a while loop.

i = 1
sum = 0
while i < 101:
     if i % 2 == 0:
        sum =sum + i
     i += 1
print(sum)
