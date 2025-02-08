

class Estate():
    def __init__(self, starting_room):
        self.rooms = []
        self.current_room = starting_room

    def add_room(self, rooms):
        for room in rooms:
            self.rooms.append(room)

    def move(self, room_name):
        # Check if the desired room is connected to the current room
        for room in self.current_room.connected_rooms:
            if room.name == room_name.name: #import rooms?
                room.times_in_room += 1
                room.visited = True
                print(room.times_in_room)
                self.current_room = room
                return
        print("You can't go that way!")