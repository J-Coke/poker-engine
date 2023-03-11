from game.Engine import PokerEngine
from game.Player import Player

def test_create_deck():
    engine = PokerEngine()
    assert len(engine.deck) == 52 
    assert isinstance(engine.deck, list)

def test_add_player_to_game():
    engine = PokerEngine()
    engine.add_player("Jeff")
    assert len(engine.players) == 1
    assert engine.players["Jeff"]["hand"] == []
    assert engine.players["Jeff"]["chips"] == 0

def test_deal_cards():
    engine = PokerEngine()
    engine.add_player("Alice")
    engine.add_player("Bob")
    engine.deal_cards()

    assert len(engine.players["Alice"]["hand"]) == 2
    assert len(engine.players["Bob"]["hand"]) == 2

    assert len(engine.deck) == 48

def test_deal_flop():
    engine = PokerEngine()
    engine.deal_flop()
    assert len(engine.board) == 3
    assert isinstance(engine.board, list)
    for card in engine.board:
        assert isinstance(card, str)