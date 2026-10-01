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

'''

# ==========================================
# Second Person - Exploration/Location
# ==========================================

# Planning
# The player can choose a location to explore.
# Locations are stored in a list.
# The player chooses a location and their current
# location is updated.


# Locations
locations = [
    "Earth",
    "Mars",
    "Asteroid Belt",
    "Space Station"
]


# Expolartion Functions
def explore(player):
    print("\n--- Available Locations ---")

    for i in range(len(locations)):
        print(str(i + 1) + ". " + locations[i])

    choice = input("Choose a location: ")

    if choice == "1":
        player["location"] = locations[0]
    elif choice == "2":
        player["location"] = locations[1]
    elif choice == "3":
        player["location"] = locations[2]
    elif choice == "4":
        player["location"] = locations[3]
    else:
        print("Invalid location.")

    print("Current location:", player["location"])





'''

'''

# ==========================================
# Third Person - Encounters/Enemies
# ==========================================

# Planning
# The player can encounter an enemy.
# The player chooses whether to fight or escape.
# The choice determines the basic outcome.


# Encounter Data
encounters = [
    "Alien",
    "Space Pirate",
    "Asteroid Creature"
]


# Encounter Function

def encounter(player):
    enemy = encounters[0]

    print("\nYou encountered:", enemy)

    print("1. Fight")
    print("2. Escape")

    choice = input("Choose an action: ")

    if choice == "1":
        print("You chose to fight.")
        print("The encounter is resolved.")

    elif choice == "2":
        print("You escaped the encounter.")

    else:
        print("Invalid choice.")


'''

'''

# ==========================================
# Fourth Person - Score / Health / Progress
# ==========================================

# Planning
# The game tracks the player's score and health.
# The game checks whether the player can continue
# or whether they have reached an ending.


# Game State
game_state = {
    "score": 0,
    "health": 100,
    "progress": 0
}


# Update Score

def update_score(game_state):
    game_state["score"] += 10
    game_state["progress"] += 1

    print("Score:", game_state["score"])
    print("Progress:", game_state["progress"])


# Check Game State
def check_game_state(game_state):

    if game_state["health"] <= 0:
        print("Game over.")

    elif game_state["progress"] >= 3:
        print("You reached the end of the game.")

    else:
        print("The game continues.")




'''
