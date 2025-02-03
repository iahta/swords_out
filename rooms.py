

class Room():
    def __init__(self, name, description, items=None, npc=None):
        self.name = name
        self.description = description
        self.connected_rooms = []
        self.items = items if items else []  # List of items in the room
        self.npc = npc  # NPC in the room (if any)
        self.corpse = False
        self.visited = False
        self.times_in_room = 0

    def add_connection(self, room):
        self.connected_rooms.append(room)

    def get_connection_names(self):
        return [room.name for room in self.connected_rooms]

    def describe(self):
        print(f"You are in the {self.name}. {self.description}")
        if self.connected_rooms:
            print("You can go to the following rooms: ", ", ".join(self.get_connection_names()))
        else:
            print("There is no way out of this room!")

class MainHall(Room):
    def __init__(self):
        super().__init__("Main Hall", "A Grandeous Hall, much to large for such a small estate.", None)
        self.visited = True
        self.times_in_room = 1
        self.furniture = ["Chair", "Bench", "Throne"]

class Library(Room):
    def __init__(self, items):
        super().__init__("Library", "Rows upon rows of dusty books.", items)
        self.furniture = ["Bookshelf", "Desk"]
class Kitchen(Room):
    def __init__(self, items):
        super().__init__("Kitchen", "The smell of food lingers, but no one's here.", items)
        self.furniture = ["Counter", "Pantry", "Cabinets"]

class Garden(Room):
    def __init__(self, items):
        super().__init__("Garden", "A beautiful outdoor garden, with flowers in bloom.", items)
       
class Dungeon(Room):
     def __init__(self, items):
        super().__init__("Dungeon", "A dark, cold dungeon filled with the echoes of chains.", items)
        self.furniture = ["Cage1", "Cage2", "chains"]

"""
### 1. Room Class:
Each room will have a name, a description, and options for which rooms can be accessed next (e.g., doors leading to other rooms).

### 2. Estate Class:
The estate will hold a collection of rooms and handle the randomization of room connections.

### 3. Player Class:
The player will need to store their current position and handle the players movement through the rooms.

Heres a basic structure to get started:

### Code:

```python



### Breakdown of the Code:

1. **Room Class**:
   - Each room has a `name`, `description`, and a list of `connected_rooms`. 
   - The `add_connection` method adds a connection to another room.
   - The `describe` method provides information about the room.

2. **Estate Class**:
   - Contains the rooms and the logic to randomize connections between them.
   - The `move` method allows the player to move between rooms.

3. **Player Class**:
   - Handles the player’s name and the action of choosing which room to go to.

4. **Randomization of Room Connections**:
   - In the `Estate.randomize_rooms()` method, room connections are randomized. For each room, it selects a random number of rooms and connects them.

5. **Game Loop**:
   - The game continues asking for input (to move to a connected room) until the player decides to stop.

### Game Flow:
- When the game starts, the player begins in the “Main Hall.”
- The estate has multiple rooms, and each room has random connections to others.
- The player can navigate the rooms, and the game will tell them where they can go next.
  
### Improvements:
- Add more detailed descriptions to the rooms.
- Add items, enemies, or puzzles in the rooms.
- Implement a quit condition or an "end game" scenario.

Does this approach look good, or would you like to tweak anything?
"""