"""
File: khansole_academy.py
-------------------------
generate 1st random number
generate 2nd random number
request user input (answer)
check if answer is correct
print 'correct' or 'incorrect'
move to next question
"""

import random

MIN_RANDOM = 10  # Start of random number series
MAX_RANDOM = 99  # End of random number series


def main():
    answer_correct = 0  # Counts the number of correct answers
    while answer_correct != '' and answer_correct != 3:  # loop escape conditions
        num1 = random.randint(MIN_RANDOM, MAX_RANDOM)  # Generates first random number
        num2 = random.randint(MIN_RANDOM, MAX_RANDOM)  # Generates second random number
        total = num1 + num2  # Adds first and second number
        print()
        print("What is " + str(num1) + " + " + str(num2) + " ? ")  # Prints the sum on the screen
        user_total = input(str("Your answer: "))  # Requests user input
        if str(total) == str(user_total):  # Checks if answer is correct, shows the correct answer and gives a message
            answer_correct += 1  # adds 1 to the 'correct answer' counter
            print()
            print("Correct!  You've gotten " + str(answer_correct) + " correct in a row")
            if answer_correct == 3:  # If the number of correct answers = 3 the program quits.
                print("Congratulations! You've mastered this.")

        else:
            print()
            print("Incorrect.  The expected answer is " + str(total))  # Prints 'incorrect answer' message.
            answer_correct = 0  # Resets the correct answer counter.


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
