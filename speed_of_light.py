

'''
queries the user for a mass in kilograms and outputs the
energy it contains in joules.
'''

SPEED_OF_LIGHT = 299792458  # c in m/s2
TNT = 0.00000000024  # Equivalent to 1 joule

def main():
    print()
    print("This program works out the energy contained in a given mass using Einstein's famous equation: E = mc2 ")
    while True:
        print()
        mass = input("Please enter a mass in Kg: ")
        energy = float(mass) * (float(SPEED_OF_LIGHT) ** 2)
        boom = (float(energy) * TNT) / 1000000
        boom = int(boom)
        print()
        print("E = mc2")
        print("Mass = " + str(mass) + " Kg")
        print("C = 299792458 m/s")
        print("Energy = " + str(energy) + " joules")
        print()
        print("That's the same as " + str(boom) + " Megatons of TNT !! ")



# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()