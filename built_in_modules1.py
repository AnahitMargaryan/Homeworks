#1.  Dice Rolling Simulator:
# Generate random numbers between 1 and 6 to simulate the roll of a six-sided die using the random module.

import random

def dice_rolling(num_dice):
    roll_result = []
    for dice in range(num_dice):
        roll = random.randint(1,6)
        roll_result.append(roll)
    return roll_result
print(dice_rolling(4))