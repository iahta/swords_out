
class Room():
    def __init__(self, name, description, weapons=None, npc=None):
        self.name = name
        self.description = description
        self.connected_rooms = []
        self.weapons = weapons if weapons else []
        self.npc = npc
        self.corpse = False
        self.visited = False
        self.times_in_room = 0


class MainHall(Room):
    def __init__(self):
        super().__init__("Main Hall", "A Grandeous Hall, much to large for such a small estate.", None)
        self.visited = True
        self.times_in_room = 1
        self.furniture = ["Chair", "Bench", "Throne"]

class Library(Room):
    def __init__(self, weapons):
        super().__init__("Library", "Rows upon rows of dusty books.", weapons)
        self.furniture = ["Bookshelf", "Desk"]

        if (self.visited == True) and (self.times_in_room > 1):
            self.description = "The air in here is still, dust settles on the books"
        elif (self.visited == True) and (self.times_in_room > 3):
            self.description = "Your movements have caused the dust to fill the air. You cough as you walk through"

class Kitchen(Room):
    def __init__(self, weapons):
        super().__init__("Kitchen", "The smell of food lingers, but no one's here.", weapons)
        self.furniture = ["Counter", "Pantry", "Cabinets"]

class Garden(Room):
    def __init__(self, weapons):
        super().__init__("Garden", "A beautiful outdoor garden, with flowers in bloom.", weapons)
       
class Dungeon(Room):
     def __init__(self, weapons):
        super().__init__("Dungeon", "A dark, cold dungeon filled with the echoes of chains.", weapons)
        self.furniture = ["Cage1", "Cage2", "chains"]