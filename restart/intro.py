import os
import textwrap

def intro():
    columns, lines = get_terminal_size()
    print("\033[31mWelcome to Swords Out!\033[0m")
    print("Swords out is a text-based detective game where you're the detective.")
    player_name = input("To get started, whats your name?\n")
    clear_screen()
    start = textwrap.fill(f"{player_name} sits hunched in a corner of their favorite tavern, The Golden Pike, as they drink away their boredom. Two years since a mystery that has really caught their interests. They could only stand to find the farmer's cow so many times.\n", width=columns)
    print(start)
    if input(f"{player_name} drinks their ale \033[33m(type drink)\033[0m \n").lower() == 'drink':
        print("something something")





def clear_screen():
    """Clears the terminal screen."""
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')

def get_terminal_size():
    try:
        size = os.get_terminal_size()
    except OSError:
        size = os.terminal_size((80, 24))  # Default size if querying fails
    return size.columns, size.lines


