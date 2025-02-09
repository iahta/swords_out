from dialogue import print_wrapped

class Evidence():
    def __init__(self, name):
        self.name = name
        self.examined = 0

class Sword(Evidence):
    def __init__(self):
        super().__init__("Sword")

    def examine(self, player):
        if self in player.evidence:
            print_wrapped("examine sword item in inventory")
        else:
            print_wrapped("You examine the sword")
            print_wrapped("Take Evidence?\n")
            action = input("1: Yes\n 2: No \n >: ")
            if action == '1':
                return True
        return False
        #return the result of the input.
        
        


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
        
        



  