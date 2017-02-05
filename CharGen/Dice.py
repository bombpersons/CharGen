import random

# Function to roll dice.
def rollDice(num, sides):
    total = 0
    for i in range(0, num):
        total += random.randint(1, sides)
    return total
