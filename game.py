import random
from player import Player
from location import Location
from questions import QUESTIONS

class Game:
    def __init__(self, num_players):
        self.players = []
        self.locations = Location.get_locations()
        self.num_players = num_players
        self.spy_index = random.randint(0, num_players - 1)
        self._assign_locations()

    def _assign_locations(self):
        locations_for_players = random.sample(self.locations, len(self.locations))
        for i in range(self.num_players):
            if i == self.spy_index:
                self.players.append(Player(name=f"Player {i+1}", location=None, is_spy=True))
            else:
                self.players.append(Player(name=f"Player {i+1}", location=locations_for_players[i], is_spy=False))

    def play_turn(self):
        for player in self.players:
            if player.is_spy:
                print(f"{player.name} is the spy!")
            else:
                print(f"{player.name} knows the location: {player.location}")

    def ask_question(self):
        for player in self.players:
            if not player.is_spy:
                question = random.choice(QUESTIONS)
                print(f"{player.name} asks: {question}")
            else:
                print(f"{player.name} is the spy and must guess!")
                # Add logic here for spy to guess location

    def check_for_winner(self):
        # Placeholder for winner logic (spy guesses or other players find the spy)
        pass
