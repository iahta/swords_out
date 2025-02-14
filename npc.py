from dialogue import *

class NPC():
    def __init__(self, name, title):
        self.name = name
        self.title = title
        self.suspect = False
        self.talked_to = False
        self.notes = []
        self.times = 1

class KingIngmar(NPC):
    def __init__(self):
        super().__init__("King Ingmar", "King of the Rothsdale Isles, Leader of Clan Tremere, Governor of Frandale")
        

    def talk(self, player):
        notes = []
        if self.times == 1:
            print_king("'Welcome Detective, I need your help. One of these four people gathered in this room is responsible for the death of the Bishop. I am hoping you can tell me who.'")
            print_wrapped(f"{player.name} takes in the site of of the King. His eyes are heavy with stress, his hair dishelved, a stark contrast to the opulent and pressed green robes that adorn his body.")
            print_wrapped(f"'I am happy to be of help your highness,' {player.name} says, 'If I may, I have a few questions.'")
            print_wrapped(f"'Where is the body?'")
            print_king("The Garden, underneath the elder tree.")
            notes.append("The body is in the Garden")
            print_wrapped(f"'And when was he found?'")
            print_king("'The Bishop was found this morning, just after the sun broke over the horizon, the Gardener found him.'")
            notes.append("The body was found in the morning.")
        
        
        self.notes.extend(notes)
        player.journal[self.name] = self.notes
        self.talked_to = True
            
        #king has win conditions all evidence

class Gardener(NPC):
    def __init__(self):
        super().__init__("Gardener Hampton", "Gardener")

    def talk(self, player):
        print("talk to hampton")
        self.talked_to = True
        self.suspect = True

class General(NPC):
    def __init__(self):
        super().__init__("General Yorbit", "General of the Isles, Commander of the King's Army")
        self.murderer = True

    def talk(self, player):
        print("talk to Yorbit")
        self.talked_to = True
        self.suspect = True

class Chef(NPC):
    def __init__(self):
        super().__init__("Chef Yanel", "Chef")

    def talk(self, player):
        print("talk to Yanel")
        self.talked_to = True

class DungeonMaster(NPC):
    def __init__(self):
        super().__init__("Executioner Rabin", "Carrier of Justice")

    def talk(self, player):
        print("talk to Rabin")
        self.talked_to = True

