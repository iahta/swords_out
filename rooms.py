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
        self.npc = []

    def talk(self, player, winning):
        if winning == True:
            print("TALKED TO ALL SUSPECTS TALK TO INGMAR, TO ARREST")
            #need win condition, suspects list? add remove suspects, suspect function npc, accuse suspect. if winning condition, and then suspect marked, you can accuse the person. 
            #winning condtion send to king ingmar. seperate function. can send back to talk more. 
        print_wrapped("you see the npcs")
        print_wrapped("who do you want to talk to?")
        for i in range(len(self.npc)):
            if self.npc[i].suspect:
                print_wrapped(f"\033[31m{i+1}: {self.npc[i].name}\033[0m\n")
            else:
                print_wrapped(f"\033[33m{i+1}: {self.npc[i].name}\033[0m\n")
        action = input(">: ")
        for j in range(len(self.npc)):
            if action == f"{j+1}":
                self.npc[j].talk(player)
        

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
            
    def search(self, player):
        print(player.evidence)
        if self.searched == 0:
            print_wrapped("You search the library first time, you see furniture and the weapon, pop funiture, with.")
            self.searched += 1
        print_wrapped("What would you like to examine? 1: Sword 2: Chair 3: Desk 4: Shelves\n")
        action = input(">: ")
        if action == "1":
            if not self.evidence:
                print_wrapped("check your inventory!")
            else:
                examined = self.evidence[0].examine(player)
                if examined:
                    popped = self.evidence.pop()
                    player.take_evidence(popped)
        elif action == "2":
            self.search_furniture("Chair")
        elif action == "3":
            self.search_furniture("Desk")
        elif action == "4":
            self.search_furniture("Shelves")
        else:
            print("Invalid Choice: Please Try Again")
            self.search()
        
    

class Kitchen(Room):
    def __init__(self):
        super().__init__("Kitchen")
        self.furniture = ["Counter, Pantry"]

    def describe(self):
        print("in the kitchen")

    def search_furniture(self, furniture):
        if furniture == "Counter":
            print_wrapped(furniture)
        if furniture == "Pantry":
            print_wrapped(furniture)
    
    def search(self, player):
        if self.searched == 0:
            print_wrapped("You search the kitchen first time, you see furniture and the weapon, pop funiture, with.")
            self.searched += 1
        print_wrapped("What would you like to examine? 1: Knife 2: Counter 3: Pantry\n")
        action = input(">: ")
        if action == "1":
            if not self.evidence:
                print_wrapped("check your inventory!")
            else:
                examined = self.evidence[0].examine(player)
                if examined:
                    popped = self.evidence.pop()
                    player.take_evidence(popped)
        elif action == "2":
            self.search_furniture("Counter")
        elif action == "3":
            self.search_furniture("Pantry")
        else:
            print("Invalid Choice: Please Try Again")
            self.search()
        #knife

class Garden (Room):
    def __init__(self):
        super().__init__("Garden")
        self.furniture = ["Bench, Tree"]
        self.corpse = []

    def describe(self):
        print("in the garden")

    def search_furniture(self, furniture):
        if furniture == "Bench":
            print_wrapped(furniture)
        if furniture == "Tree":
            print_wrapped(furniture)

    def search(self, player):
        if self.searched == 0:
            print_wrapped("You search the garden first time, you see furniture and the weapon, pop funiture, with.")
            self.searched += 1
        print_wrapped("What would you like to examine? 1: Rope 2: Corpse 3: Bench 4: Tree\n")
        action = input(">: ")
        if action == "1":
            if not self.evidence:
                print_wrapped("check your inventory!")
            else:
                examined = self.evidence[0].examine(player)
                if examined:
                    popped = self.evidence.pop()
                    player.take_evidence(popped)
        elif action == "2":
            self.corpse[0].examine()
        elif action == "3":
            self.search_furniture("Bench")
        elif action == "4":
            self.search_furniture("Tree")
        else:
            print("Invalid Choice: Please Try Again")
            self.search()
        #rope

class Dungeon (Room):
    def __init__(self):
        super().__init__("Dungeon")
        self.furniture = ["Cage, Chains"]

    def describe(self):
        print("in the dungeon")

    def search_furniture(self, furniture):
        if furniture == "Cage":
            print_wrapped(furniture)
        if furniture == "Chair":
            print_wrapped(furniture)

    def search(self, player):
        if self.searched == 0:
            print_wrapped("You search the dungeon first time, you see furniture and the weapon, pop funiture, with.")
            self.searched += 1
        print_wrapped("What would you like to examine? 1: Shield 2: Cage 3: Chains\n")
        action = input(">: ")
        if action == "1":
            if not self.evidence:
                print_wrapped("check your inventory!")
            else:
                examined = self.evidence[0].examine(player)
                if examined:
                    popped = self.evidence.pop()
                    player.take_evidence(popped)
        elif action == "2":
            self.search_furniture("Cage")
        elif action == "3":
            self.search_furniture("Chains")
        else:
            print("Invalid Choice: Please Try Again")
            self.search()
        #shield

