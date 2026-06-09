import sys
rooms = {
    'Town': ['Forest'],
    'Forest': ['Town', 'Cave'],
    'Cave': ['Forest', 'Castle'],
    'Castle': ['Cave']
}
items = {
    'Forest':'sword',
    'Cave':'shield',
    'Castle':'treasure',
    'Town':'map'
}

current_room = 'Forest'
inventory = []

def show_room(room,exit_rooms,items_rooms):
    print("What would you like to do? (ex: Forest, Town, sword)")
    print("Current room: " + room)
    print("Connected rooms: " + str(exit_rooms[room]))
    if room in items.keys():
        print("You see a " + items_rooms[room])




def player_inventory(players_inventory):
    if not players_inventory:
        print("Inventory is empty.")
    else:
        print("Inventory: ")
        print(str(inventory))

def take_item(item):
    del items[current_room]
    inventory.append(str(item))
    print(item + " placed in inventory")

def process_command(command):
    if command == "exit":
        print("Exit game.")
        sys.exit()
    elif command == "inventory":
        player_inventory(inventory)
    elif command in rooms.keys():
        move_player(command)
    elif command in items.values():
        take_item(command)

def move_player(destination):
    global current_room
    if destination in rooms[current_room]:
        current_room = destination
        print("Heading to: " + current_room)
        if destination == "Castle":
            if "shield" in inventory and "sword" in inventory:
                check_win()

def check_win():
    print("you won the game!")
    sys.exit()

while True:
    show_room(current_room,rooms,items)
    choice = input(">")
    process_command(choice)
