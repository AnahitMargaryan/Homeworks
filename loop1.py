# Exercise 1: Counting Even Numbers

numbers = [1,10,15,14,11,13,18,22,28,15]
count = 0 
for digits in numbers:
    if digits % 2 == 0:
        count += 1
print(count)