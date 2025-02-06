from rooms import Room
from estate import Estate
from player import Player
from create_rooms import *
import textwrap
import os



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
        user_input = input("What would you like to do? (exit, move, or search): ").strip().lower()

        if user_input == "exit":
            print("Thank you for playing!")
            break
        elif user_input == "move":
            player.take_action(estate)
        elif user_input == "search":
            #take account of items to search
            print("searching")

def game():
    Intro, directions on how to exit and move around Drink! 
    start 
    player name
    a murder happens
    create rooms (add weapons, distribute npcs, evidence, corpse, the story of the murder)
    ivestigate, clues, talk to suspects
    review inventory and clues
    king- have you come to a conclusion
    guards take away the murderer
    victory! 




class Game():
    def __init__(self):
        self.running = True
        self.locations = []
        self.player = Player("Adventurer")
        self.create_world()
        

    def create_world(self):
       
        estate
        main room = MainHall
        libraryroom = Library
        dungeonroom = Dungeon 
        kitchenroom = Kitchen 
        bedroom = Bedroom 

        npc1 = King
        npc2 = Cook
        npc2 = LadyKinsington
        npc3 = Governor Hacksmith
        npc4 = Advisor Kennedy
        corpse = Bishop Thompson

        libraryroom.add_enemy(goblin)

        estate = add rooms to estate

    def clear_screen(self):
    #Clears the terminal screen.
        if os.name == 'nt':
            _ = os.system('cls')
    # For macOS and Linux
        else:
            _ = os.system('clear')

    def print_wrapped(text):
    # Get the width of the terminal dynamically
        width = os.get_terminal_size().columns
    # Wrap the text
        wrapped_text = textwrap.fill(text, width)
    # Print the wrapped text
        print(wrapped_text)

    def intro(self):
        self.print_wrapped("\033[31mWelcome to Swords Out!\033[0m\n")
        self.print_wrapped("Swords out is a text-based detective game where you're the detective.")
        self.player.name = input("Start detecting, whats your name?\n")
        self.clear_screen()
        self.print_wrapped(f"{self.player.name} sits hunched in a corner of their favorite tavern, The Golden Pike, as they drink away their boredom. Two years since a mystery that has really caught their interests. They could only stand to find the farmer's cow so many times.\n")
        self.print_wrapped(f"{self.player.name} drinks their ale \033[33m(type drink)\033[0m \n")
        if input(">: ").strip().lower == 'drink':
            self.print_wrapped("The tavern was lively. Lucky, the tavern owner, paraded around his establishment conversing with every patron. He knew not to mess with {player_name}. Especailly when they didn't have a case.")
            self.print_wrapped(f"{self.player.name} took another drink, the ale filling the hole left by their need to investigate. \033[33m(type drink)\033[0m \n")
            if input(">: ") == 'drink':
                self.print_wrapped(f"The tavern door burst open. Soldiers clad in shining, clean armor filled the tavern. The leader spoke, 'Where is {self.player.name}?'")
                self.print_wrapped(f"{self.player.name} held their hand up. Finishing their drink. \033[33m(type drink)\033[0m \n")
                if input(">: ") == 'drink':
                        #soldier talk

    def run(self):
        self.intro()

        while self.running:
            # Describe current location
            self.player.location.describe()

            # Get player action
            action = input("\nWhat would you like to do? (move, pickup, fight, quit): ").strip().lower()

            if action == "move":
                # Move to another location
                print("\nAvailable locations to move to:")
                for idx, location in enumerate(self.locations):
                    print(f"{idx + 1}. {location.name}")
                choice = int(input("Choose a location (1-2): ")) - 1
                new_location = self.locations[choice]
                self.player.move(new_location)

            elif action == "pickup":
                # Pickup an item
                if self.player.location.items:
                    print("\nItems available to pick up:")
                    for idx, item in enumerate(self.player.location.items):
                        print(f"{idx + 1}. {item.name}")
                    choice = int(input("Choose an item (1-2): ")) - 1
                    item = self.player.location.items.pop(choice)
                    self.player.add_item(item)
                else:
                    print("\nNo items here to pick up.")

            elif action == "fight":
                # Fight an enemy
                if self.player.location.enemies:
                    print("\nEnemies available to fight:")
                    for idx, enemy in enumerate(self.player.location.enemies):
                        print(f"{idx + 1}. {enemy.name}")
                    choice = int(input("Choose an enemy to fight (1-2): ")) - 1
                    enemy = self.player.location.enemies.pop(choice)
                    print(f"\nYou are fighting {enemy.name}!")
                    while enemy.health > 0 and self.player.health > 0:
                        enemy.attack(self.player)
                        if self.player.health > 0:
                            print(f"\nYou attacked {enemy.name}!")
                            enemy.health -= 10
                        if enemy.health <= 0:
                            print(f"\nYou defeated {enemy.name}!")
                            break
                else:
                    print("\nNo enemies here to fight.")

            elif action == "quit":
                self.running = False
                print("\nYou quit the game.")

            else:
                print("\nInvalid action, please try again.")

# Start the game
"""game = Game()
game.run()"""
