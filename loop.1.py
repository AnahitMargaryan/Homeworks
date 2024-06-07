#Exercise 1. Print the even numbers from 0 to 20 using a for loop and the range function.

even = []
for number in range(0,21):
    if number % 2 == 0: 
        even.append(number)    
print(even)