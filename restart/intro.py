import os
import textwrap


def intro(columns, player_name):  
    clear_screen()
    start = textwrap.fill(f"{player_name} sits hunched in a corner of their favorite tavern, The Golden Pike, as they drink away their boredom. Two years since a mystery that has really caught their interests. They could only stand to find the farmer's cow so many times.\n", width=columns)
    print(start)
    if input(f"{player_name} drinks their ale \033[33m(type drink)\033[0m \n").lower() == 'drink':
        print(textwrap.fill(f"The tavern was lively. Lucky, the tavern owner, paraded around his establishment conversing with every patron. He knew not to mess with {player_name}. Especailly when they didn't have a case.", width=columns))
        if input(textwrap.fill(f"{player_name} took another drink, the ale filling the hole left by their need to investigate. \033[33m(type drink)\033[0m \n", width=columns)).lower() == 'drink':
            print(textwrap.fill(f"The tavern door burst open. Soldiers clad in shining, clean armor filled the tavern. The leader spoke, 'Where is {player_name}?'"))
            if input(textwrap.fill(f"{player_name} held their hand up. Finishing their drink. \033[33m(type drink)\033[0m \n")).lower() == 'drink':
                clear_screen()
                print(textwrap.fill(f"{player_name} alalalal", width=columns))
    
   
        



def clear_screen():
    """Clears the terminal screen."""
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')




