from rooms import Room
from estate import Estate
from player import Player
from create_rooms import *

def main():
    # Create rooms
    rooms = create_rooms()
    # Start with the Main Hall room
    estate = Estate(rooms[0])
    # Randomize connections between rooms
    estate.rooms.extend(rooms[1:])
    estate.randomize_rooms()
    # Create player
    player = Player("Adventurer")
    # Game loop
    while True:
        user_input = input("What would you like to do? (exit, move, or search)").strip().lower()

        if user_input == "exit":
            print("Thank you for playing!")
            break
        elif user_input == "move":
            player.take_action(estate)
        elif user_input == "search":
            #take account of items to search
            print("searching")

"""  while True:
        player.take_action(estate)     
        # If the player wants to quit, break the loop
        if input("Do you want to continue exploring? (y/n): ").lower() != "y":
            print("Thanks for playing!")
            break
"""
if __name__ == "__main__":
    main()



### **Text-Based Adventure Game Pseudo Code**
"""
Program: TextBasedAdventureGame
Start

    // Initialize the game world
    Create rooms (Room objects with description and possible exits)
    Create player (Player object with inventory, health, etc.)

    Print "Welcome to the Adventure Game!"

    // Main game loop
    while player is alive and has not completed the game then
        Print current room description
        Show possible actions (e.g., "Go North", "Pick up item", "Talk to NPC", etc.)
        
        Get player input (command: go [direction], take [item], talk, etc.)
        
        if command is a direction (e.g., go north) then
            if the direction is valid then
                Move player to the next room
                Print description of the new room
            else
                Print "You can't go that way!"
                
        else if command is "take [item]" then
            if the item is in the current room then
                Add item to player's inventory
                Remove item from the room
                Print "[item] has been added to your inventory."
            else
                Print "There is no such item here."
        
        else if command is "talk" then
            if there is an NPC in the room then
                Engage in conversation with NPC (NPC may give hints, quests, etc.)
                Print NPC dialogue
            else
                Print "There is no one to talk to here."
                
        else if command is "use [item]" then
            if the item is in player's inventory then
                Perform action with the item (e.g., unlock a door, heal player, etc.)
                Print appropriate result of using the item
            else
                Print "You don't have that item."
        
        else if command is "look" then
            Print detailed description of the current room
            Show items in the room
        
        else if command is "inventory" then
            Print player's inventory (list of items they have collected)
        
        else if command is invalid then
            Print "Invalid command. Try again."

        // Check if player has completed the game or if they have died
        if player completes the game (e.g., finds the treasure, defeats the boss) then
            Print "Congratulations, you won the game!"
            End game
        
        if player health reaches 0 then
            Print "You have died. Game Over."
            End game
        
End
```

---

### **Detailed Breakdown:**

1. **Game World (Rooms, Items, NPCs):**
   - **Rooms:** The game world is made up of different "rooms," each containing a description, possible exits (e.g., North, South, East, West), items, and possibly NPCs (Non-Player Characters).
   - **Items:** Rooms may contain items that the player can pick up, which might be useful later in the game.
   - **NPCs:** Characters the player can talk to. They might provide useful information, items, or quests.

2. **Player Actions:**
   - **Movement (go [direction]):** The player can move from one room to another, provided theres an exit in that direction.
   - **Item Interaction (take [item], use [item]):** The player can pick up items found in rooms and later use them when necessary.
   - **Look:** A command to examine the room, which will show all available items, exits, and descriptions.
   - **Inventory:** The player can check their inventory to see what items they have.

3. **Game Flow:**
   - The game loop continues as long as the player has not won or died. Inside the loop, the game waits for player input, processes that input, and updates the game state.
   - Winning conditions can include finding a special item (e.g., treasure) or defeating an NPC boss.
   - The player can "die" if they encounter a game-ending scenario (e.g., losing all health).

4. **End Game Conditions:**
   - The game ends either when the player wins (e.g., completes the quest) or when the player dies (e.g., loses all health).
   - After the game ends, a message is displayed, and the game terminates.

---
### **Example Python Implementation**
def play_game():
    # Create rooms
    room1 = Room("You are in a dark forest. The path splits to the north and east.", {'north': None, 'east': None}, ['sword'])
    room2 = Room("You are in a clearing. There is a cave to the west and a path leading south.", {'west': None, 'south': None}, ['shield'])
    room3 = Room("You find yourself at the entrance of a dungeon.", {'south': None}, [])

    # Add exits
    room1.exits['north'] = room2
    room2.exits['west'] = room3

    # Create player and NPCs
    player = Player(name="Adventurer")
    npc = NPC(name="Old Man", dialogue="Beware of the monster in the dungeon!")

    # Set current room
    current_room = room1

    print("Welcome to the Adventure Game!")

    while player.health > 0:
        # Show current room description and options
        print(current_room.description)
        print("Exits: ", ", ".join(current_room.exits.keys()))
        print("Items here:", ", ".join(current_room.items))
        if current_room.npc:
            print("You see an NPC: ", current_room.npc.name)

        action = input("What do you want to do? ")

        if action.startswith("go "):
            direction = action.split(" ")[1]
            if direction in current_room.exits:
                current_room = current_room.exits[direction]
            else:
                print("You can't go that way!")
        
        elif action.startswith("take "):
            item = action.split(" ")[1]
            if item in current_room.items:
                player.take_item(item)
                current_room.items.remove(item)
                print(f"You took the {item}.")
            else:
                print("There is no such item here.")
        
        elif action == "look":
            print(current_room.description)

        elif action == "inventory":
            print("You have:", ", ".join(player.inventory))

        elif action == "talk" and current_room.npc:
            current_room.npc.talk()
        
        else:
            print("Invalid command. Try again.")

        # Check for win or death conditions
        if player.health <= 0:
            print("You have died. Game over.")
            break

        # You can add more conditions for winning, like finding a treasure or defeating a boss

    print("Game Over!")

# Run the game
play_game()
```

---

### **Key Features of the Example:**

- **Room class**: Represents rooms in the game, each containing a description, exits, items, and possibly an NPC.
- **Player class**: Handles the players health and inventory.
- **NPC class**: Provides dialogue that the player can interact with.
- **Game Loop**: The game runs in a loop, continuously asking for the player's actions and updating the game state based on input.
  
This is a basic framework for a text-based adventure game. You can expand it by adding puzzles, combat, more complex interactions, and a larger world to explore.

"""