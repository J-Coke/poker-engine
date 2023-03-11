from game.Player import Player

def test_init_player():
    player = Player("Alice")
    assert player.name == "Alice"
    assert player.hand == []
    assert player.chips == 0
