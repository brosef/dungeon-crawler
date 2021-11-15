'''
    Ask the player for their name.
    Display a message that greets them and introduces them to the game world.
    Present them with a choice between two doors.
    If they choose the left door, they'll see an empty room.
    If they choose the right door, then they encounter a dragon.
    In both cases, they have the option to return to the previous room or interact further.
    When in the seemingly empty room, they can choose to look around. If they do so, they will find a has_sword. They can choose to take it or leave it.
    When encountering the dragon, they have the choice to fight it.
    If they have the has_sword from the other room, then they will be able to defeat it and win the game.
    If they don't have the has_sword, then they will be eaten by the dragon and lose the game.
'''
prompt = ">> "

# quest start conditions
has_sword = False
is_alive = True
complete = False
location = ""

name = input(f"Adventurer! Declare yourself! What is thine name? {prompt}")
print(f"Welcome {name}, to the final leg of your journey.")

while not complete:
    location = input(f"You face two identical doors to your left and your right. Which do you choose? {prompt}")
    while location != "left" and location != "right" and location != "outside":
        location = input(f"Sorry adventurer, {location} makes no sense. Please choose 'left or 'right' {prompt}")
        continue
    print(f"You open the {location} door and enter.")
    while location == "left":
        action = input(f"You see an empty room. What would you like to do? {prompt}")
        while action != "look" and action != "inspect" and action != "leave":
            action = input(f"Not sure what you meant there. You can 'look', 'inspect', or 'leave' {prompt}")
            break
        if action == ("look" or "inspect"):
            if not has_sword:
                print("You find a sword hidden in some rubbish. You take it.")
                has_sword = True
                continue
            else:
                print("Just some freshly disturbed rubbish here.")
                continue
        else:
            print("You leave the empty room.")
            location = "outside"
            break

    while location == "right":
        action = input(f"You see a MASSIVE dragon curled up in the middle of the room. "
                       f"What would you like to do? {prompt}")
        while action != "fight" and action != "leave":
            action = input(f"Not sure what you meant there. You can 'fight' or 'leave' {prompt}")
            break
        if action == "fight":
            if not has_sword:
                print("Since you don't have a weapon, you sneak up to the dragon and punch it on its butt. "
                      "The dragon awakens and burns you to a crisp.")
                is_alive = False
                complete = True
                break
            else:
                print("You run up to the dragon, ram your sword into its neck and neatly slice its jugular. "
                      "Blood sprays everywhere in a heavy mist. You smile.")
                complete = True
                break
        else:
            location = "outside"
            break

if is_alive is False:
    print(f"{name.upper()}. Punching a dragon on its butt is not a good idea. You should have been wielding some kind "
          "of weapon.")
else:
    print(f"The dragon has been slayed, {name}! You are victorious!")
