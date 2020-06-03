"""
File: liftoff.py
----------------------
This program writes out the calls for a spaceship that is about to launch.
It counts down the numbers from 10 to 1 and then writes “Liftoff!”
"""
import time  # imports the time library


#  the program counts down from 10 to 1 then prints "lift off"

def main():
    x = 11  # Counter starts at countdown value + 1.
    for i in range(10):  # Repeats 10 times.
        x -= 1  # deducts 1 from the counter.
        print(x)  # Prints the counter value to screen.
        time.sleep(1)  # Pauses 1 second.
    print("Lift off!")  # prints 'Lift off!'.


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()
