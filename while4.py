# Write a Python program that generates a random number between 1 and 100 and asks
# the user to guess the number. The program should give hints whether the guessed
# number is too high or too low until the correct number is guessed.


import random
num = random.randint(1, 100)
while True:
    print('Guess a number between 1 and 100')
    guess = input()
    i = int(guess)
    if i == num:
        print('You won!!!')
        break
    elif i < num:
               print('Try Higher')
    elif i > num:
               print('Try Lower')