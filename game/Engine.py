import random
from game.Player import Player

class PokerEngine:
    def __init__(self):
        self.deck = self.create_deck()
        self.players = {}

    def create_deck(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['h', 'c', 'd', 's']
        deck = []
        for rank in ranks:
            for suit in suits:
                deck.append(rank + suit)
        random.shuffle(deck)
        return deck

    def add_player(self, name, chips=0):
        player = Player(name, chips)
        self.players[player.name] = {"chips": player.chips, "hand": player.hand}

    def deal_cards(self):
        for i in range(2):
            for player in self.players.values():
                card = self.deck.pop()
                player["hand"].append(card)