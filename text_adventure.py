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
    'Town':'key'
}

current_room = 'Forest'
inventory = []
def show_room(room,exit_rooms,items_rooms):
    print("Commands: Town, sword, inventory, look, exit")
    print("Current room: " + room)
    print("Connected rooms: " + str(exit_rooms[room]))
    if room in items.keys():
        print("You see a " + items_rooms[room])


def player_inventory(players_inventory):
    if not players_inventory:
        print("Inventory is empty.")
    else:
        for item in players_inventory:
            print("-" + item)

def take_item(item):
    if items.get(current_room) == item:
        del items[current_room]
        inventory.append(str(item))
        print(item + " placed in inventory")
    else:
        print("That item does not exist in this location.")

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
    elif command == "look":
        show_room(current_room,rooms,items)
    else:
        print("Invalid command.")
def move_player(destination):
    global current_room
    if destination in rooms[current_room]:
        current_room = destination
        print("Heading to: " + current_room)
        if destination == "Castle":
            if "shield" in inventory and "sword" in inventory:
                check_win()
    else:
        print("You can't go there from here.")

def check_win():
    print("you won the game!")
    sys.exit()

show_room(current_room,rooms,items)

while True:
    choice = input(">")
    process_command(choice)

