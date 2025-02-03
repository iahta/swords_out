from rooms import Room
from estate import Estate
from player import Player
from create_rooms import *


def game():
  # Create rooms
    rooms = create_rooms()
    # Start with the Main Hall room
    estate = Estate(rooms[0])
    # Randomize connections between rooms
    estate.rooms.extend(rooms[1:])
    estate.randomize_rooms()
    # Create player
    player = Player("Adventurer")
    # Game loop
    while True:
        user_input = input("What would you like to do? (exit, move, or search)").strip().lower()

        if user_input == "exit":
            print("Thank you for playing!")
            break
        elif user_input == "move":
            player.take_action(estate)
        elif user_input == "search":
            #take account of items to search
            print("searching")
