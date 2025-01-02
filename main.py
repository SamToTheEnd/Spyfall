from game import Game

def start_game():
    num_players = int(input("Enter the number of players: "))
    game = Game(num_players)

    print("\nThe game is starting...\n")
    game.play_turn()

    while True:
        game.ask_question()
        action = input("\nWould you like to continue the game? (yes/no): ").strip().lower()
        if action == "no":
            break

if __name__ == "__main__":
    start_game()
