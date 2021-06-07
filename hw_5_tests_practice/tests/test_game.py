import pytest
from hw_5_tests_practice.game import TicTacToe


def setup_module(module):
    global game_test
    game_test = TicTacToe()
    game_test.board[4] = "X"


def test_available_moves():
    assert 4 not in game_test.available_moves()
    assert 3 in game_test.available_moves()

    with pytest.raises(AssertionError):
        assert -1 in game_test.available_moves()


def test_make_move():
    assert game_test.make_move(4, "X") is False
    assert game_test.make_move(5, "X") is True

    with pytest.raises(IndexError):
        assert game_test.make_move(9, "X") is False

    assert game_test.board[5] != " "
    assert game_test.board[7] == " "

