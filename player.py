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
        print("\n")
        #estate.current_room.describe()
        available_choices = estate.current_room.get_connection_names()
        ### action to move rooms###
        if available_choices:
            print("You can go to the following rooms: ", ", ".join(available_choices))
            for i in range(len(available_choices)):
                print(f"{(i+1)}: {available_choices[i]}\n")
            choice = input('>:')
            if choice.lower() == '1':
                estate.move(available_choices[0])
            elif choice.lower() == '2':
                estate.move(available_choices[1])
            elif choice.lower() == '3':
                estate.move(available_choices[2])
            elif choice.lower() == '4':
                 estate.move(available_choices[3])
            else:
                print("There is no way out of this room!\n")
            ###pause menu if anything other than the choices listed###
        else:
            ###YOUREDEAD###
            print("You can't go anywhere.")

        
    
        
