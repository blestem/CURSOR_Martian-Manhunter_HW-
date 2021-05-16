import unittest
from hw_5_tests_practice.game import TicTacToe

import HTMLTestRunner
import xmlrunner


class TestWinner(unittest.TestCase):
    def setUp(self):
        self.game = TicTacToe()

    def test_win_row(self):
        self.game.board = ["X", "X", "X", " ", " ", " ", " ", " ", " "]
        self.assertTrue(self.game.winner(2, "X"))
        self.game.board = [" ", " ", " ", "X", "X", "X", " ", " ", " "]
        self.assertTrue(self.game.winner(5, "X"))
        self.game.board = [" ", " ", " ", " ", " ", " ", "X", "X", "X"]
        self.assertTrue(self.game.winner(8, "X"))

    def test_win_column(self):
        self.game.board = ["X", " ", " ", "X", " ", " ", "X", " ", " "]
        self.assertTrue(self.game.winner(0, "X"))
        self.game.board = [" ", "X", " ", " ", "X", " ", " ", "X", " "]
        self.assertTrue(self.game.winner(1, "X"))
        self.game.board = [" ", " ", "X", " ", " ", "X", " ", " ", "X"]
        self.assertTrue(self.game.winner(2, "X"))

    def test_win_diagonal1(self):
        self.game.board = ["X", " ", " ", " ", "X", " ", " ", " ", "X"]
        self.assertTrue(self.game.winner(0, "X"))

    def test_win_diagonal2(self):
        self.game.board = [" ", " ", "X", " ", "X", " ", "X", " ", " "]
        self.assertTrue(self.game.winner(2, "X"))

    def test_win_not_won(self):
        self.game.board = ["X", "0", "X", " ", " ", " ", "X", " ", " "]
        self.assertFalse(self.game.winner(0, "X"))


if __name__ == "__main__":
    unittest.main()




