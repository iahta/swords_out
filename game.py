
import os
from dialogue import print_wrapped
from player import Player
from rooms import *
from estate import Estate
from corpse import Corpse
from npc import *

class Game():
    def __init__(self):
        self.running = True
        self.locations = []
        self.player = Player("Detective Reed")
        self.corpse = Corpse()
        self.library = Library()
        self.dungeon = Dungeon()
        self.garden = Garden()
        self.kitchen = Kitchen()
        self.main_hall = MainHall()
        self.estate = Estate(self.main_hall)
        #add other npcs
        self.king = KingIngmar()
        self.gardener = Gardener()
        self.general = General()
        self.dungeon_master = DungeonMaster()
        self.chef = Chef()
        self.npcs = [self.king, self.gardener, self.general, self.dungeon_master, self.chef]
        #add other evidence
        self.sword = Sword()
        self.rope = Rope()
        self.shield = Shield()
        self.knife = Knife()
        self.win = False

        self.create_world()
        
    def create_world(self):
        self.estate.add_room([self.main_hall, self.library, self.dungeon, self.kitchen, self.garden])
        self.main_hall.connected_rooms = [self.library, self.kitchen]
        self.library.connected_rooms = [self.main_hall, self.garden]
        self.kitchen.connected_rooms = [self.main_hall, self.dungeon]
        self.garden.connected_rooms = [self.library]
        self.dungeon.connected_rooms = [self.kitchen]
        self.garden.corpse.append(self.corpse)

        #add other evidence
        self.library.evidence.append(self.sword)
        self.kitchen.evidence.append(self.knife)
        self.garden.evidence.append(self.rope)
        self.dungeon.evidence.append(self.shield)
        
        #add other npcs
        self.main_hall.npc.append(self.king)
        self.main_hall.npc.append(self.gardener)
        self.main_hall.npc.append(self.general)
        self.main_hall.npc.append(self.dungeon_master)
        self.main_hall.npc.append(self.chef)

        self.winning = all([self.king.talked_to, self.gardener.talked_to, self.general.talked_to, self.dungeon_master.talked_to, self.chef.talked_to])

    

    def clear_screen(self):
    #Clears the terminal screen.
        if os.name == 'nt':
            _ = os.system('cls')
    # For macOS and Linux
        else:
            _ = os.system('clear')


    def intro(self):
        print_wrapped("\033[31mWelcome to Swords Out!\033[0m\n")
        print_wrapped("Swords out is a text-based detective game where you're the detective.")
        print_wrapped("Start detecting, whats your name?\n")
        self.player.name = input(">: ")
        self.clear_screen()
        print_wrapped(f"{self.player.name} sits hunched in a corner of their favorite tavern, The Golden Pike, as they drink away their boredom. Two years since a mystery that has really caught their interests. They could only stand to find the farmer's cow so many times.\n")
        print_wrapped(f"{self.player.name} drinks their ale \033[33m(type drink)\033[0m \n")
        if input(">: ").strip().lower == 'drink':
            print_wrapped("The tavern was lively. Lucky, the tavern owner, paraded around his establishment conversing with every patron. He knew not to mess with {player_name}. Especailly when they didn't have a case.")
        print_wrapped(f"{self.player.name} took another drink, the ale filling the hole left by their need to investigate. \033[33m(type drink)\033[0m \n")
        if input(">: ") == 'drink':
            print_wrapped(f"The tavern door burst open. Soldiers clad in shining, clean armor filled the tavern. The leader spoke, 'Where is {self.player.name}?'")
        print_wrapped(f"{self.player.name} held their hand up. Finishing their drink. \033[33m(type drink)\033[0m \n")
        if input(">: ") == 'drink':
            print("hello")#soldier talk
    
    def arrest(self):
        for i in range(len(self.npcs)):
            if self.npcs[i].suspect:
                print_wrapped(f"{i+1}: {self.npcs[i].name}")
        action = input(">: ")
        for j in range(len(self.npcs)):
            if action == f"{j+1}":
                if self.npcs[j].murderer:
                    print("Congrats! You caught the murderer!")
                    self.running = False
        

    def win_condition(self):
        if all(npc.talked_to for npc in self.npcs):
            self.win = True
            print_wrapped("You've talked to all Suspects, do you have enough evidence to arrest?")
            print_wrapped("1: Yes\n2: No")
            action = input(">: ")
            if action == "1":
                self.arrest()
            elif action == "2":
                print_wrapped("Happy Hunting")
        else:
            print_wrapped("You need to talk to all suspects first.")

    def run(self):
        self.intro()

        while self.running:
            #desribe location self.player.location.desribe()
            current_room = self.estate.current_room
            current_room.describe()
            if current_room.name == "Main Hall":
                self.win_condition()
                if not self.running:
                    break
                action = input("What would you like to do? \n 1: Talk 2: Move 3: Search 4: Inventory Q: Quit\n>: ").strip().lower()
                if action == "1":
                    self.main_hall.talk(self.player)#npcs are listed in the main hall #pass in player to take notes in journal 
                elif action == "2":
                   self.player.move(self.estate)
                elif action == "3":
                    print_wrapped("You look over the main hall, the npcs sit")
                elif action == "4":
                    self.player.view_inventory()
                elif action == "q":
                    self.running = False
                    print("You Quit The Game")
                else:
                    print("\nInvalid Action, Please Try Again")
            else:
                action = input("What would What would you like to do? \n 1: Move 2: Search 3: Inventory Q: Quit\n>: ").strip().lower()
                if action == "1":
                    self.player.move(self.estate)
                elif action == "2":
                    self.estate.current_room.search(self.player)
                elif action == "3":
                    self.player.view_inventory()            
                elif action == "q":
                    self.running = False
                    print("You Quit The Game")
                else:
                    print("\nInvalid Action, Please Try Again")
            
