# Import the random library to use for the dice later
import random

# Write a Python dictionary to define the following powers of a monster
# along with their corresponding strength values:
powersForMonster = {"Fire Magic": 2, "Freeze Time": 4, "Super Hearing": 6}

belt = []

# Hero's Attack Functions
def hero_attacks(combat_strength, m_health_points):
    ascii_image = """
                                @@   @@ 
                                @    @  
                                @   @   
               @@@@@@          @@  @    
            @@       @@        @ @@     
           @%         @     @@@ @       
            @        @@     @@@@@     
               @@@@@        @@       
               @    @@@@                
          @@@ @@                        
       @@     @                         
   @@*       @                          
   @        @@                          
           @@                                                    
         @   @@@@@@@                    
        @            @                  
      @              @                  
      """
    print(ascii_image)
    print("Player's weapon (" + str(combat_strength) + ") ---> Monster (" + str(m_health_points) + ")")
    if combat_strength >= m_health_points:
        m_health_points = 0
        print("You have killed the monster")
    else:
        m_health_points -= combat_strength
        print("You have reduced the monster's health to " + str(m_health_points))
    return m_health_points


# Monster's Attack Function
def monster_attacks(m_combat_strength, health_points):
    ascii_image2 = """                                                                 
           @@@@ @                           
      (     @*&@  ,                         
    @               %                       
     &#(@(@%@@@@@*   /                      
      @@@@@.                                
               @       /                    
                %         @                 
            ,(@(*/           %              
               @ (  .@#                 @   
                          @           .@@. @
                   @         ,              
                      @       @ .@          
                             @              
                          *(*  *      
             """
    print(ascii_image2)
    print("Monster's Claw (" + str(m_combat_strength) + ") ---> Hero (" + str(health_points) + ")")
    if m_combat_strength >= health_points:
        health_points = 0
        print("You have killed the monster")
    else:
        health_points -= m_combat_strength
        print("The monster has reduced your health to " + str(health_points))
    return health_points


# Game
# Define The number of lives for the Hero and Monster
numLives = 10  # number of player's lives remaining
mNumLives = 12  # number of monster's lives remaining

# Define the Dice
diceOptions = list(range(1, 7))
# Define the Weapons
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]

# Print out the weapons using a for loop
for weapon in weapons:
    print(weapon)

# Roll for Monster's Magic Power
input("Roll the dice for Monster's Magic Power (Press enter)")
randomPower = random.choice(list(powersForMonster.keys()))
print("The monster's magic power is" + randomPower + 
      " with a strength of " +str(powersForMonster[randomPower]))

# Update Monster's Combat Strength based on rolled power
m_combat_strength = random.randint(1, 6)
combat_strength = m_combat_strength
original_strength = m_combat_strength
m_combat_strength = min(6, m_combat_strength + powersForMonster[randomPower])
print("Updated Monster's Combat Strength: " + str(m_combat_strength) + 
      " (Original Strength: " + str(original_strength) + ", Power Used: " + randomPower + ")")

# Define the Loot
loot_options = ["Health Potion", "Poison Potion", "Secret Note", "Leather Boots", "Flimsy Gloves"]
good_loot_options = ["Health Potion", "Leather Boots"]
bad_loot_options = ["Poison Potion"]

# Define the number of stars awarded to the Player
num_stars = 0

# Use a While Loop to get valid input for Hero and Monster's Combat Strength
i = 0

while i in range(5):
    combat_strength = input("Enter your combat Strength (1-6): ")
    m_combat_strength = input("Enter the monster's combat Strength (1-6): ")

    # Validate input: Check if the string inputted is numeric
    if (not combat_strength.isnumeric()) or (not m_combat_strength.isnumeric()):
        # If one of the inputs are invalid, print error message and halt
        print("One or more invalid inputs. Player needs to enter integer numbers for Combat Strength")
        i = i + 1
        continue

    # Note: Now safe to cast combat_strength to integer
    # Validate input: Check if the string inputted is a number between 1-6
    elif (int(combat_strength) not in range(1, 7)) or (int(m_combat_strength)) not in range(1, 7):
        print("Enter a valid integer between 1 and 6 only")
        i = i + 1
        continue

    # Break out of while loop if input was valid
    else:
        break

# Input was valid - broke out of while loop
combat_strength = int(combat_strength)
m_combat_strength = int(m_combat_strength)

# Roll for weapon
input("Roll the dice for your weapon (Press enter)")
weaponRoll = random.choice(diceOptions)

# Max out the combat strength at 6
combat_strength = min(6, (combat_strength + weaponRoll))
print("The hero\'s weapon is " + str(weapons[weaponRoll - 1]))

# Weapon Roll Analysis
input("Analyze the Weapon roll (Press enter)")
if weaponRoll <= 2:
    print("--- You rolled a weak weapon, friend")
elif weaponRoll <= 4:
    print("--- Your weapon is meh")
else:
    print("--- Nice weapon, friend!")

# If the weapon rolled is not a Fist, print out "Thank goodness you didn't roll the Fist..."
if weapons[weaponRoll - 1] != "Fist":
    print("--- Thank goodness you didn't roll the Fist...")

# Roll for player health points
input("Roll the dice for your health points (Press enter)")
health_points = random.choice(diceOptions)
print("Player rolled " + str(health_points) + " health points")

# Roll for monster health points
input("Roll the dice for the monster's health points (Press enter)")
m_health_points = random.choice(diceOptions)
print("Player rolled " + str(m_health_points) + " health points for the monster")

input("Analyze the roll (Press enter)")
# Compare Player vs Monster's strength
print("--- You are matched in strength: " + str(combat_strength == m_combat_strength))

# Check the Player's overall strength and health
print("--- You have a strong player: " + str((combat_strength + health_points) >= 15))

max_health_points = 6

# Loop while the monster and the player are alive. Call fight sequence functions
print("You meet the monster. FIGHT!!")
while m_health_points > 0 and health_points > 0:

    input("You strike first (Press Enter)")
    m_health_points = hero_attacks(combat_strength, m_health_points)
    if m_health_points == 0:
        num_stars = 3
        # The player finds a loot bag after defeating the monster
        print("You have defeated the monster and found a loot bag! Roll for your first item.")
        input("Press Enter to roll for an item...")
        if loot_options:
            selected_index = random.randint(0, len(loot_options) - 1)
            selected_item = loot_options.pop(selected_index)
            belt.append(selected_item)
            print("You have obtained: " + selected_item)
            print("Items in your belt now: " + str(belt))

            # Second loot item
            input("Press Enter to roll for another item...")
            if loot_options:
                selected_index = random.randint(0, len(loot_options) - 1)
                selected_item = loot_options.pop(selected_index)
                belt.append(selected_item)
                print("You have obtained: " + selected_item)
                print("Items in your belt now: " + str(belt))

            # Organizing the loot belt
            print("Organizing the belt alphabetically...")
            belt.sort()
            print("Items in your organized belt: ", str(belt))
        else:
            print("No more items to loot!")

        if belt:
            used_item = belt.pop(0)  # Remove and store the first item
            print(f"You use: {used_item}")

            # Check if the item is good or bad and adjust health accordingly
            if used_item in good_loot_options:
                health_points = min(max_health_points, health_points + 2)  # Increase health but not over max
                print(f"The {used_item} boosts your health to {health_points}.")
            elif used_item in bad_loot_options:
                health_points = max(0, health_points - 2)  # Decrease health but not below 0
                print(f"The {used_item} harms you, reducing your health to {health_points}.")
            else:
                print("The item was not helpful in this situation.")

            # Display the player's updated health points
            print(f"Your current health points: {health_points}")
        else:
            print("Your belt is empty! You have no items to use.")
    else:
        input("The monster strikes (Press Enter)")
        health_points = monster_attacks(m_combat_strength, health_points)
        if health_points == 0:
            num_stars = 1
        else:
            num_stars = 2

stars = "*" * num_stars
print("Hero gets <" + stars + "> stars")
