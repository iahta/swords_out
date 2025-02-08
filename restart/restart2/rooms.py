from dialogue import print_wrapped

class Room():
    def __init__(self, name):
        self.name = name
        self.connected_rooms = []
        self.visited = False
        self.times_in_room = 0

    def get_connection_names(self):
        return [room.name for room in self.connected_rooms]
    

class MainHall(Room):
    def __init__(self):
        super().__init__("Main Hall")
        self.visited = True
        self.furniture = ["Chair", "Bench", "Throne"]

    def describe(self):
        if self.times_in_room > 1:
            print_wrapped(f"You are in the {self.name}. A Grandeous Hall, much to large for such a small estate.")
        elif self.times_in_room > 3:
            print_wrapped(f"You are in the {self.name}. The midday sun highlights the golden tapestry cascading down from the windows.")

class Library(Room):
    def __init__(self):  
        super().__init__("Library")
        self.furniture = ["Bookshelf", "Desk"]

class Kitchen(Room):
    def __init__(self):
        super().__init__("Kitchen")
        self.furniture = ["Counter", "Pantry", "Cabinets"]

class Garden (Room):
    def __init__(self):
        super().__init__("Garden")

class Dungeon (Room):
    def __init__(self):
        super().__init__("Dungeon")
        self.furniture = ["Cage1", "Cage2", "chains"]