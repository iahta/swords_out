from dialogue import print_wrapped

class Corpse():
    def __init__(self):
        self.name = "Bishop Havdin"
        self.evidence = ["bruises on the abdomen", "stab wounds", "rope burn on wrists"]


    def bruises(self):
        print_wrapped("examine the bruises")

    def wounds(self):
        print_wrapped("examine the stab wounds")

    def burns(self):
        print_wrapped("examine the rope burns")

    def examine(self):
        print_wrapped(f"you examine the corpse, \033[31m{self.evidence[0]}\033[0m, \033[31m{self.evidence[1]}\033[0m, \033[31m{self.evidence[2]}\033[0m")
        print_wrapped("would you like to take a closer look? 1: Bruises, 2: Stab Wounds 3: Burns")
        action = input(">: ")
        if action == "1":
            self.bruises()
        elif action == "2":
            self.wounds()
        elif action == "3":
            self.burns()
        else:
            print_wrapped("Not an Option, Please Try Again")
            self.examine()
