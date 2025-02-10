from dialogue import print_wrapped

class NPC():
    def __init__(self, name, title):
        self.name = name
        self.title = title
        self.suspect = False

class KingIngmar(NPC):
    def __init__(self):
        super().__init__("King Ingmar", "King of the Rothsdale Isles, Leader of Clan Tremere, Governor of Frandale")

    def talk(self):
        print("talk to ingmar")

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

