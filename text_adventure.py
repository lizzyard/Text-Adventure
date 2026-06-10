import sys, random
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
moves = 0
score = 0



    
def show_room(room,exit_rooms,items_rooms):
    print("Commands: Town, sword, inventory, look, exit")
    print("Current room: " + room)
    print("Connected rooms: " + str(exit_rooms[room]))
    print("Total moves: " + str(moves))
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
        global score
        if item != 'treasure':
            points_earned = 10
            score += 10
            print("You earned: " + str(points_earned) + " points!")
        elif item == 'treasure':
            points_earned = 50
            score += 50
            print("You earned: " + str(points_earned) + " points!")
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
    global moves
    if destination in rooms[current_room]:
        if destination == 'Castle' and "shield" in inventory and "sword" in inventory:
            current_room = destination
            moves += 1
            print("Heading to: " + current_room)
            return True
        elif destination != 'Castle':
            current_room = destination
            moves += 1
            print("Heading to: " + current_room)
            return True
        else:
            print("You need the shield and sword in order the enter the Castle.")
            return False
    else:
        print("You can't go there from here.")
        return False

def check_win():
    if "treasure" in inventory:
        print("you won in " + str(moves) + "!")
        sys.exit()

show_room(current_room,rooms,items)

while True:
    choice = input(">")
    process_command(choice)

    




