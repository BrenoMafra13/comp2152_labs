# Lab 2 questions
# Student Name: Breno Lopes Mafra
# Student ID: 101485572

import random

# Defining array with 6 weapons
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"]

# Defining function
def main():
    try:
        print(input("Press enter to roll the dice"))
        weaponRoll = random.randint(1,6)
        hero_weapon = weapons[weaponRoll - 1]

        if weaponRoll != 0 and weaponRoll <= 2:
            print(f"You rolled a weak weapon ({hero_weapon}), friend")
        elif weaponRoll != 0 and weaponRoll <= 4:
            print(f"Your weapon ({hero_weapon}) is meh")
        elif weaponRoll != 0 and weaponRoll <= 6:
            print(f"Nice weapon ({hero_weapon}), friend!")
        else:
            print(f"Thank goodness you didn't roll the Fist, you got ({hero_weapon})")
    except ValueError as e:
        print(f"Error: {e}")

# Run the game
if __name__ == "__main__":
    main()