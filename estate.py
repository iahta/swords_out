import random
from pprint import pprint

class Estate():
    def __init__(self, starting_room):
        self.rooms = []
        self.current_room = starting_room
        self.add_room(starting_room)

    def add_room(self, room):
        self.rooms.append(room)

    def move(self, room_name):
        # Check if the desired room is connected to the current room
        for room in self.current_room.connected_rooms:
            if room.name == room_name: #import rooms?
                room.times_in_room += 1
                print(room.times_in_room)
                self.current_room = room
                return
        print("You can't go that way!")

    def randomize_rooms(self):
        """Randomize connections between rooms"""
        for room in self.rooms:
            random_connected_rooms = random.sample(self.rooms, random.randint(1, len(self.rooms)-1))
            for connected_room in random_connected_rooms:
                if connected_room != room:
                    room.add_connection(connected_room)
