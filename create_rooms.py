from rooms import *
import random

def murder_weapon():
    weapons = ["knife", "sword", "shield", "rope"]
    random.shuffle(weapons)
    return weapons

def create_rooms():
    weapons = murder_weapon()
    """Helper function to create rooms for the estate."""
    room1 = MainHall()
    room2 = Library(weapons[0])
    room3 = Kitchen(weapons[1])
    room4 = Garden(weapons[2])
    room5 = Dungeon(weapons[3])
    return [room1, room2, room3, room4, room5]

"""build classes for each
Use a case switch to build out each room. Setting inital values an radomizing all
of the items and evidence, then build out the descriptions based on rather a room has
been visited
need to clean up play loop
"""
