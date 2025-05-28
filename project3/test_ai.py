import unittest
from ai import GameAI
from board import Board

class DummyBoard(Board):
    """Subclass the Board for easier test setup."""
    def set_state(self, grid):
        self.grid = grid

class TestGameAI(unittest.TestCase):
    def setUp(self):
        self.ai = GameAI("AI", "O")
        self.board = DummyBoard()

    def test_ai_selects_only_legal_moves(self):
        """Test that the AI only selects unoccupied positions."""
        # Fill some positions; only few left
        grid = [
            ["X", "O", "X"],
            ["X", "O", ""],
            ["O", "", ""]
        ]
        self.board.set_state(grid)
        # AI must only select empty cells
        for _ in range(10):
            move = self.ai.get_move(self.board)
            self.assertIn(move, [(1, 2), (2, 1), (2, 2)])
            self.assertTrue(self.board.is_valid_move(*move))

    def test_ai_returns_none_when_no_moves(self):
        """Test AI returns None if the board is full."""
        grid = [
            ["X", "O", "X"],
            ["O", "X", "O"],
            ["O", "X", "X"]
        ]
        self.board.set_state(grid)
        move = self.ai.get_move(self.board)
        self.assertIsNone(move)

if __name__ == "__main__":
    unittest.main()
