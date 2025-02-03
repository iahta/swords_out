from game import game
def main():
    print("Welcome to Swords Out!")
    if input("Type Start to begin the game: ").lower() != "start":
        game()
if __name__ == "__main__":
    main()