

class NPC():
    def __init__(self, name, dialogue):
        self.name = name
        self.dialogue = dialogue
        self.is_innoncent = True

    def talk(self):
        print(self.dialogue)

    def killer(self, weapon):
        self.is_innoncent = False
        self.murder_weapon = weapon
        