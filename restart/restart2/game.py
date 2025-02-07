import textwrap
import os
from player import Player

class Game():
    def __init__(self):
        self.running = True
        self.locations = []
        self.player = Player("Detective Reed")
        #self.create_world()
        
    #def create_world():
        #MainHall
        #library
        #dungeonroom
        #garden
        #estate

        #create npcs
        #create and add corpse 
        #add npcs to rooms

    def clear_screen(self):
    #Clears the terminal screen.
        if os.name == 'nt':
            _ = os.system('cls')
    # For macOS and Linux
        else:
            _ = os.system('clear')

    def print_wrapped(self, text):
    # Get the width of the terminal dynamically
        width = os.get_terminal_size().columns
    # Wrap the text
        wrapped_text = textwrap.fill(text, width)
    # Print the wrapped text
        print(wrapped_text)

    def intro(self):
        self.print_wrapped("\033[31mWelcome to Swords Out!\033[0m\n")
        self.print_wrapped("Swords out is a text-based detective game where you're the detective.")
        self.print_wrapped("Start detecting, whats your name?\n")
        self.player.name = input(">: ")
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
            print("hello")#soldier talk
    
    def run(self):
        self.intro()

        while self.running:
            #desribe location self.player.location.desribe()

            action = input("What would you like to do? \n 1: Talk 2: Move 3: Search Q: Quit\n>: ").strip().lower()

            if action == "1":
                #talk
            elif action == "2":
                #move
            elif action = "3":
                #search
            elif action == "q":
                self.running = False
                print("Your Quit The Game")
            else:
                print("\nInvalid Action, Please Try Again")
            
