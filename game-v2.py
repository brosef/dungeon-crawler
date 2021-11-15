# TODO: offload room, item, and creature data to json
# TODO: success = all creatures slayed
# TODO: implement functions
# TODO: implement item attributes
# Save the user input options you allow e.g. in a set that you can check against when your user makes a choice.
import random

allowed_verbs = {"look", "open", "pick up", "west", "east", "north", "south", "fight", "run", "inv"}

# Create an inventory for your player, where they can add and remove items.

inv = []
# Players should be able to collect items they find in rooms and add them to their inventory.

# If they lose a fight against the dragon, then they should lose their inventory items.

#inv.clear()
#current_room = rooms[0]

# Add more rooms to your game and allow your player to explore.

room0 = {
    "name": "entry",
    "description": "You're standing in a room. There is a door to the north",
    "creatures": {},
    "items": {},
    "exits": {
        "north": 1
    }
}

room1 = {
    "name": "empty",
    "description": "This is an empty room. There is a door to the west and south.",
    "creatures": {},
    "items": [
        "Dagger",
        "Health Potion"
    ],
    "exits": {
        "west": 2,
        "south": 0
    },
}

room2 = {
    "name": "sewer",
    "description": "This is a room with a foul odor. There is a door to the east.",
    "creatures": {
        "fetid monster": {
            "hp": 1,
            "description": "big, oozing lump of a creature.",
        }
    },
    "items": [
        "Fetid Key"
    ],
    "exits": {
        "east": 1
    }
}

room3 = {
    "name": "Room with door",
    "creatures": {},
    "items": [],
    "description": "A locked door is to your North. There is a door to the east.",
    "exits": {
        "east": 2
    }
}

rooms = [room0, room1, room2, room3]
# Some rooms can be empty, others can contain items, and yet others can contain an opponent.
current_room = rooms[0]
complete = False

while not complete:
    # let's spit out current room attributes
    print(current_room["description"])
    if current_room["items"]:
        print("In this room you see: ")
        for x in current_room["items"]:
            print(f"a {x}")
    if current_room["creatures"]:
        print(f"You see a {current_room['creatures']}")

    # capture player input and test against all items in allowed_verbs
    player_choice = input('what would you like to do?: ')
    if player_choice not in allowed_verbs:
        print("I don't understand that choice. Try again.")
        continue
    if player_choice in current_room["exits"].keys():
        x = current_room["exits"][player_choice]
        current_room = rooms[x]
        continue
    elif player_choice == "pick up":
        for f in current_room["items"]:
            if f in inv:
                print(f"You already have a(n) {f}")
            else:
                inv.append(f)
                current_room["items"] = ""
    elif player_choice == "inv":
        print("Your inventory contains:")
        for x in inv:
            print(f"a {x}")
    else:
        print("You can't go there.")
        continue


# Implement some logic that decides whether or not your player can beat the opponent depending on what items they have
# in their inventory



# Use the random module to add a multiplier to your battles, similar to a dice roll in a real game. This pseudo-random
# element can have an effect on whether your player wins or loses when battling an opponent.

#print(inv)

#if inv["weapons"]["dagger"]["power"] > 1:
#    print("You win!")
