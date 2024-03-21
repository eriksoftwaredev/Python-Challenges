from random import randint
from collections import Counter

def roll_dice(*dice, num_trials = 1_000_000):
    sides_count = len(dice)
    counts = Counter(sum(randint(1, sides) for sides in dice) for _ in range(num_trials))

    print('\nOUTCOME\tPROBABILITY')
    for outcome in range(sides_count, sum(dice) + 1):
        print(f'{outcome}\t{counts[outcome] * 100 / num_trials :0.2f}%')

# Test the function:
roll_dice(4, 6, 6)
roll_dice(4, 6, 6, 20)
