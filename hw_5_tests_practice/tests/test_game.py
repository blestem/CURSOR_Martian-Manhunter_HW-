import pytest
from hw_5_tests_practice.game import TicTacToe

game = TicTacToe()
game.board[4] = "X"


def test_available_moves():
    assert (4 not in game.available_moves())


def test_make_move():
    assert game.make_move(4, "X") is False
    assert game.make_move(5, "X") is True
    assert game.board[5] != " "
