
class Player():
    def __init__(self, name):
        self.name = name
        self.inventory = []

    def take_item (self,item):
        self.inventory.append(item)
    
    def move(self, estate):
        #need estate, current room, connecting rooms
        
