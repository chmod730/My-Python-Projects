"""
File: random_numbers.py
-----------------------
This program prints a series of random numbers in the
range from MIN_RANDOM to MAX_RANDOM, inclusive
"""

import random

NUM_RANDOM = 10  # the number of random numbers to be generated
MIN_RANDOM = 0  # Start of random number series
MAX_RANDOM = 100  # End of random number series


def main():
    for i in range(NUM_RANDOM):  # Repeats to the value of NUM_RANDOM.
        x = random.randint(MIN_RANDOM, MAX_RANDOM)  # Picks a number between MIN & MAX and calls it x.
        print(x)  # Prints the value of x.


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
