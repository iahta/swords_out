from dialogue import print_wrapped


class Player():
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.evidence = []

    def take_item (self,item):
        self.inventory.append(item)
    
    def take_item (self,evidence):
        self.evidence.append(evidence)
    
    def move(self, estate):
        available_choices = estate.current_room.connected_rooms
        print_wrapped("You can go to the following rooms: ")
        for i in range(len(available_choices)):
            print_wrapped(f"{(i+1)}: {available_choices[i].name}\n")
            
        choice = input('>:')
        if choice.lower() == '1':
            estate.move(available_choices[0])
        elif choice.lower() == '2':
            estate.move(available_choices[1])
        else:
            print("There is no way out of this room!\n")

    
        

