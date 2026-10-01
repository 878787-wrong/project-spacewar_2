# ==========================================
# Aishwarya - Players/Actions
# ==========================================
#
# Planning:
# Purpose:
# - Allow the player to control the spaceship.
#
# Player data:
# - name
# - health
# - oil
# - location
#
# Process:
# 1. Display the player's current state.
# 2. Display available actions.
# 3. Ask the player to choose an action.
# 4. Check which action they selected.
# 5. Perform the action.
# 6. Update the player's state.
# 7. Continue until the player chooses to quit.
#


# COLLECTIONS
# Create a dictionary containing the player's information.
player = {
    "name": "Player", #Planning to allow user to input their own main during User interface
    "health": 100,
    "oil": 5,
    "location": "Earth"
}

# Create a list containing the available actions.
actions = [
    "Explore",
    "Attack",
    "Repair",
    "Inspect Ship"
]


# FUNCTIONS

def inspect_ship(player):
    print("Player:", ________)
    print("Health:", ________)
    print("Oil:", ________)
    print("Location:", ________)
    
    pass


def perform_action(player, choice):

    if choice == "1":
        print("You chose to explore.")

    elif choice == "2":
        print("You chose to attack.")

    elif choice == "3":
        print("You chose to repair.")

    elif choice == "4":
        inspect_ship(player)

    else:
        print("Invalid choice.")


# CONTROL FLOW
# Keep asking the player for an action until
# they decide to stop.

playing = True

while playing:

    print("\nChoose an action:")

    for i in range(len(actions)):
        print(str(i + 1) + ".", actions[i])

    choice = input("Enter your choice: ")

    perform_action(player, choice)

    continue_game = input("Continue? (y/n): ")

    if continue_game.lower() == "n":
        playing = False
