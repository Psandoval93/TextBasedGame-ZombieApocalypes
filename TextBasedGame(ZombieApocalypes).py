# Phillip Sandoval

# The dictionary links a room to other rooms.
rooms = {
    'Living Room': {'South': 'Hallway', 'North': 'Bedroom', 'East': 'Dining Room', 'West': 'Front Porch'},
    'Hallway': {'North': 'Living Room', 'East': 'Garage', 'Item': 'Flashlight'},
    'Bedroom': {'South': 'Living Room', 'East': 'Bathroom', 'Item': 'Rifle'},
    'Dining Room': {'North': 'Kitchen', 'West': 'Living Room', 'Item': 'Knife'},
    'Garage': {'West': 'Hallway', 'Item': 'Ammo'},
    'Bathroom': {'West': 'Bedroom', 'Item': 'FirstAid'},
    'Kitchen': {'South': 'Dining Room', 'Item': 'Food'},
    'Front Porch': {'East': 'Living Room', 'Item': 'Zombies'}  # Item = Villain
}


# Printing instructions
def game_instructions():
    print('Welcome to "The Rise of the Zombie Apocalypse"')
    print('Collect all 6 items to defeat the zombies, or your brains will be eaten.')
    print('Move commands are: go North, go South, go East, go West')
    print('To end game type "exit"')
    print('To add item to Inventory enter: get "item name"')


# Defining variable to move between rooms with parameter
def moving_rooms(direction, current_room):
    # Creating if statement looking for variable within dictionary
    if direction in rooms[current_room]:
        current_room = rooms[current_room][direction]  # Setting variable to room based on reference
    else:  # Creating else statement when if statement conditions not met
        print('You have entered an invalid move. Please try again.')  # Printing error message
    return current_room  # Returns current room


# Defining the function to get item
def get_item(item, item_inventory):
    item_inventory.append(item)  # Adding item to inventory
    print(item, 'has been added to the inventory')  # Printing string updating inventory


# Defining main function
def main():
    game_instructions()  # Calling game_instructions function
    current_room = 'Living Room'  # Creates variable default
    inventory = []  # Creates empty inventory list
    user_move = ""  # Creates empty string

    # Creating main loop with while statement &  creating conditions
    while user_move != 'exit':

        # Creates if statement checking room and if all items collected
        if current_room == 'Front Porch' and len(inventory) == 6:
            print('You have defeated the zombies! Congrats you win!')  # Prints if user wins
            break  # Loop ends

        # Creates if statement checking room and if all items collected
        if current_room == 'Front Porch' and len(inventory) != 6:
            print('You’re not prepared the zombies ate your brains! Nom ! Game Over! Try Again')  # Prints if user loses
            break  # Loop ends

        # Creates if statement checking if item is in current room
        if "Item" in rooms[current_room]:
            if not rooms[current_room]["Item"] in inventory:  # If item not in inventory
                print('You see a', rooms[current_room]['Item'])  # Prints item you see in room
        print('You are in the', current_room)  # Prints where user is
        print('Inventory:', inventory)  # Prints inventory list
        user_move = input('What would you like to do?')  # Asks for and receives user input
        user_choice = user_move.split()  # Splits user input
        if len(user_choice) == 2 and  user_choice[0] == 'go':  # Checks index 0 for string 'go'
            direction = user_choice[1]  # If statement is true takes index 1 as direction
            current_room = moving_rooms(direction, current_room)  # Uses direction to determine current room

        elif len(user_choice) == 2 and user_choice[0] == 'get':  # Checks index 0 for string 'get'
            item = user_choice[1]  # If statement is true takes index 1 as item

            # If/else statement checks if item in room not in inventory list
            if item in rooms[current_room]['Item'] and item not in inventory:
                get_item(item, inventory)  # passes user_choice[1] to get_item()
            else:
                # Prints statement when if statement conditions not met
                print('You entered an invalid item or the item you entered is not in this room.')
        else:
            print('Invalid input, please enter "go" or "get" plus item or direction you want.')


main()  # Calls main function
print('Thank you for playing! You have exited the game.')  # Prints thank you message after game is exited
