from dialogue import print_wrapped

class Evidence():
    def __init__(self, name):
        self.name = name

class Sword(Evidence):
    def __init__(self):
        super().__init__("Sword")

    def examine(self):
        print_wrapped("You examine the sword")


class Knife(Evidence):
    def __init__(self):
        super().__init__("Knife")

    def examine(self):
        print_wrapped("You examine the knife")

class Shield(Evidence):
    def __init__(self):
        super().__init__("Shield")

    def examine(self):
        print_wrapped("You examine the shield")

class Rope(Evidence):
    def __init__(self):
        super().__init__("Rope")

    def examine(self):
        print_wrapped("You examine the rope")
        
        



  