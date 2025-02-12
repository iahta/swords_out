from dialogue import print_wrapped


class Player():
    def __init__(self, name):
        self.name = name
        self.evidence = []
        self.journal = {} #dictionary- Name: list of notes from talking
        

    def write_note (self,item):
        self.journal.append(item)
    
    def take_evidence (self,evidence):
        self.evidence.append(evidence)
    
    def move(self, estate):
        available_choices = estate.current_room.connected_rooms
        print_wrapped("You can go to the following rooms: ")
        for i in range(len(available_choices)):
            if available_choices[i].visited: 
                print_wrapped(f"\033[36m{(i+1)}: {available_choices[i].name}\033[0m\n")
            else:
                print_wrapped(f"\033[31m{(i+1)}: {available_choices[i].name}\033[0m\n")
        choice = input('>:')
        if choice.lower() == '1':
            estate.move(available_choices[0])
        elif choice.lower() == '2':
            estate.move(available_choices[1])
        else:
            print("There is no way out of this room!\n")

    def view_journal(self):  #need to add way to mark suspects
        if self.journal:
            name_list = list(self.journal)
            for i in range(len(name_list)):
                print_wrapped(f"{i+1}: {name_list[i]}")
            journal_notes = input(">: ")
            for j in range(len(name_list)):
                if journal_notes == f"{j+1}":
                    for note in self.journal[name_list[j]]:
                        print_wrapped(note)
                else:
                    print_wrapped("Not an Option, Please Try Again")
                    self.view_journal()
        else:
            print_wrapped("Talk to the Suspects in the Main Hall")
    
    def view_inventory(self): #suspects list?
        print_wrapped("1: Journal 2: Weapons")
        action = input(">: ")
        if action == "1":
            self.view_journal()
            #pass in the class npc? a list of all of them? #how to pass in the notes themselves
        elif action == "2":
            if self.evidence:
                for i in range(len(self.evidence)):
                    print_wrapped(f"{i + 1}: {self.evidence[i].name}")
                action = input(">: ")
                if action == "1":
                    self.evidence[0].examine(self)
                elif action == "2":
                    self.evidence[1].examine(self)
                elif action == "3":
                    self.evidence[2].examine(self)
                elif action == "4":
                    self.evidence[3].examine(self)
                else:
                    print_wrapped("Not an Option Please Try Again")
                    self.view_inventory()
        else:
            print_wrapped("Evidence is Currently Empty\n")

        #need to add other evidence to obtain.
        #journal
            #index
                #evidence, furniture, suspect notes, 
        #weapons

        


        

        

    
        

