from dialogue import print_wrapped

class NPC():
    def __init__(self, name, title):
        self.name = name
        self.title = title
        self.suspect = False
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
        self.suspect = True
        #king has win conditions all evidence

class Gardener(NPC):
    def __init__(self):
        super().__init__("Gardener Hampton", "Gardener")

    def talk(self):
        print("talk to hampton")

class General(NPC):
    def __init__(self):
        super().__init__("General Yorbit", "General of the Isles, Commander of the King's Army")

    def talk(self):
        print("talk to Yorbit")

class Chef(NPC):
    def __init__(self):
        super().__init__("Chef Yanel", "Chef")

    def talk(self):
        print("talk to Yanel")

class DungeonMaster(NPC):
    def __init__(self):
        super().__init__("Executioner Rabin", "Carrier of Justice")

    def talk(self):
        print("talk to Rabin")

