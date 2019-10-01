import random
import sys

def roll():
    result = random.randrange(1, 7)
    print("Dice Rolled. Result = ", result)
    return result

def roll_n_dice(num_dice):
    print("Rolling ", num_dice, " Dice...")
    result = 0
    for _ in range(num_dice):
        result += roll()
    print("All Dice Rolled. Result = ", result)
    return result

def cmd_roll():
    if len(sys.argv) != 2:
        raise Exception("Usage: roll-many <num-dice>")
    roll_n_dice(int(sys.argv[1]))
