import unittest
from ai_player import AIPlayer
from board import Board

class DummyBoard:
    """
    Dummy Board class for testing AIPlayer independently of the real Board implementation.
    Implements only what's required for AIPlayer's get_move method.
    """
    def __init__(self, cells):
        self.cells = cells
    def is_cell_empty(self, row, col):
        return self.cells[row][col] == ' '

class TestAIPlayer(unittest.TestCase):
    def setUp(self):
        self.ai = AIPlayer('O')

    def test_ai_moves_are_legal(self):
        board_state = [
            ['O', 'X', 'O'],
            ['X', ' ', ' '],
            [' ', ' ', 'X']
        ]
        board = DummyBoard(board_state)
        for _ in range(10):
            move = self.ai.get_move(board)
            self.assertIsNotNone(move)
            r, c = move
            self.assertTrue(board.is_cell_empty(r, c))

    def test_ai_handles_full_board(self):
        board_state = [
            ['O', 'X', 'O'],
            ['X', 'X', 'O'],
            ['O', 'O', 'X']
        ]
        board = DummyBoard(board_state)
        move = self.ai.get_move(board)
        self.assertIsNone(move)

    def test_ai_single_move_left(self):
        board_state = [
            ['O', 'X', 'O'],
            [' ', 'X', 'O'],
            ['O', 'O', 'X']
        ]
        board = DummyBoard(board_state)
        move = self.ai.get_move(board)
        self.assertEqual(move, (1, 0))

if __name__ == '__main__':
    unittest.main()
