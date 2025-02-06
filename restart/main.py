#from game import game
from intro import intro
import os

def main():
    def get_terminal_size():
        try:
            size = os.get_terminal_size()
        except OSError:
            size = os.terminal_size((80, 24))  # Default size if querying fails
        return size.columns, size.lines
    
    columns, lines = get_terminal_size()
    print("\033[31mWelcome to Swords Out!\033[0m\n")
    print("Swords out is a text-based detective game where you're the detective.")
    player_name = input("Start detecting, whats your name?\n") #everything above this, needs to go to main
    ##player name, class creation
    ##create estate
    intro(columns, player_name)
    """print("Welcome to Swords Out!")
    if input("Type Start to begin the game: ").lower() != "start":
        game()"""
    
    
if __name__ == "__main__":
    main()