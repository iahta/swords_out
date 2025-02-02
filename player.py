from estate import Estate

class Player():
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        self.inventory = []

    def take_item(self, item):
        self.inventory.append(item)

    def use_item(self, item):
        if item in self.inventory:
            # Define what happens when the item is used (e.g., heal, unlock, etc.)
            pass
        else:
            print("You don't have that item.")

    def take_action(self, estate):
        print("\nWhat would you like to do?")
        estate.current_room.describe()
        available_choices = estate.current_room.get_connection_names()
        if available_choices:
            choice = input(f"Where would you like to go? {', '.join(available_choices)}: ")
            estate.move(choice)
        else:
            print("You can't go anywhere.")
    
