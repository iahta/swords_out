from dialogue import print_wrapped

class NPC():
    def __init__(self, name, title):
        self.name = name
        self.title = title
        self.suspect = False
        self.talked_to = False
        self.notes = []

class KingIngmar(NPC):
    def __init__(self):
        super().__init__("King Ingmar", "King of the Rothsdale Isles, Leader of Clan Tremere, Governor of Frandale")

    def talk(self, player):
        print("talk to ingmar")
        note1 = "Note 1"
        note2 = "Note 2"
        note3 = "Note 3"
        notes = [note1, note2, note3]
        self.notes.extend(notes)
        player.journal[self.name] = self.notes
        print(player.journal)
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

