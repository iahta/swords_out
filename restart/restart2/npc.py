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