"""
File: moon_weight.py
--------------------
This program will ask a user to enter their weight on Earth
Then tell them their weight on the Moon.
"""


def main():
    num1 = float(input("Enter a weight on Earth: "))  # Requests user input.  Uses Real Numbers.
    num2 = float(num1) * 0.165  # Calculates weight on moon.
    print("Equivalent weight on the moon: " + str(num2))  # Prints answer to screen in Real Numbers.


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
