"""
Nimm is an ancient game of strategy that is named after the old German word for "take."
It is also called Tiouk Tiouk in West Africa and Tsynshidzi in China. Players alternate
taking stones until there are zero left. The game of Nimm goes as follows:
1. The game starts with a pile of 20 stones between the players
2. The two players alternate turns
3. On a given turn, a player may take either 1 or 2 stone from the center pile
4. The two players continue until the center pile has run out of stones.
The last player to take a stone loses.
"""


#  Checks the value entered is either a 1 or 2
def check_value(choice, stone_count):
    while choice != 1 and choice != 2:
        choice = int(input("Please enter a 1 or 2: "))
    else:
        stone_count = stone_count - choice
        return stone_count


# tells player 1 how many stones are left and asks how many stones to remove.
def ask_player_1(stone_count):
    print()
    print("There are " + str(stone_count) + " stones left")
    choice = int(input("Player 1 would you like to remove 1 or 2 stones? "))
    while int(choice) > stone_count:  # Checks the value entered is not more than the available stones.
        print()
        choice = int(input("There is only 1 stone left.  Please select 1: "))
    else:
        stone_count = check_value(choice, stone_count)
    return stone_count


# tells player 2 how many stones are left and asks how many stones to remove.
def ask_player_2(stone_count):
    print()
    print("There are " + str(stone_count) + " stones left")
    choice = int(input("Player 2 would you like to remove 1 or 2 stones? "))
    while int(choice) > stone_count:
        print()
        choice = int(input("There is only 1 stone left.  Please select 1: "))
    else:
        stone_count = check_value(choice, stone_count)
    return stone_count


def main():
    stone_count = 20  # Starting number of stones.
    player_counter = 0  # Determines who's turn it is. PLayer 1 = 0. Player 2 = 1.
    while stone_count != 0 and stone_count != -1:  # Sets conditions for game to run.
        if player_counter == 0:
            stone_count = ask_player_1(stone_count)  # Asks Player 1 question.
            player_counter = 1  # Sets player counter to player 2
        else:
            stone_count = ask_player_2(stone_count)  # Asks Player 2 question.
            player_counter = 0  # Sets player counter to player 1

#  Determines the winner and prints message
    else:
        if player_counter == 0:
            print()
            print("Player 1 wins!")
        if player_counter == 1:
            print()
            print("Player 2 wins!")


if __name__ == '__main__':
    main()
