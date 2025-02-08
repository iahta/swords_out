from dialogue import print_wrapped
from evidence import *

class Room():
    def __init__(self, name):
        self.name = name
        self.connected_rooms = []
        self.items = []
        self.evidence = []
        self.visited = False
        self.times_in_room = 0
        self.searched = 0

    def get_connection_names(self):
        return [room.name for room in self.connected_rooms]
    

class MainHall(Room):
    def __init__(self):
        super().__init__("Main Hall")
        self.visited = True
        self.times_in_room = 1

    def describe(self):
        if self.times_in_room >= 1 and self.times_in_room <= 2:
            print_wrapped("You are in the Main Hall. A Grandeous Hall, much to large for such a small estate.")
        if self.times_in_room >= 3:
            print_wrapped("You are in the Main Hall. The midday sun highlights the golden tapestry cascading down from the windows.") 

class Library(Room):
    def __init__(self):  
        super().__init__("Library")
        self.furniture = ["Chair, Desk, Shelf"]

    def describe(self):
        print("in the Library")

    def search_furniture(self, furniture):
        if furniture == "Shelf":
            print_wrapped(furniture)
        if furniture == "Desk":
            print_wrapped(furniture)
        if furniture == "Chair":
            print_wrapped(furniture)
            
    def search(self):
        if self.searched == 0:
            print("You search the library first time, you see furniture and the weapon, pop funiture, with.")
            self.searched += 1
        if self.evidence:
            print_wrapped("What would you like to examine? 1: Sword 2: Chair 3: Desk 4: Shelf\n")
        elif not self.evidence:
            print_wrapped(what would you like to examine?)
        if self.furniture:
            if self.evidence:
                print with evidence: 
        action = input(">: ")
        if action == 
    

class Kitchen(Room):
    def __init__(self):
        super().__init__("Kitchen")

    def describe(self):
        print("in the kitchen")
    
    def search(self):
        print("you search the kitchen")
        #knife

class Garden (Room):
    def __init__(self):
        super().__init__("Garden")

    def describe(self):
        print("in the garden")

    def search(self):
        print("you search the garde")
        #rope

class Dungeon (Room):
    def __init__(self):
        super().__init__("Dungeon")

    def describe(self):
        print("in the dungeon")

    def search(self):
        print("you search the dungeon")
        #shield

