import random
from typing import Optional, Tuple

class TicTacToeAI:
    """
    Simple Tic Tac Toe AI implementing basic strategies:
    1. Take the win if possible
    2. Otherwise, block the opponent's win if possible
    3. Otherwise, make a random valid move
    """

    def __init__(self, symbol: str):
        """
        Args:
            symbol (str): The symbol for the AI ('X' or 'O')
        """
        self.symbol = symbol
        self.opponent_symbol = 'O' if symbol == 'X' else 'X'

    def select_move(self, board) -> Optional[Tuple[int, int]]:
        """
        Returns the next AI move as a tuple (row, col), or None if no move is possible.
        The AI applies (in order): win-if-possible, block-if-needed, then random.

        Args:
            board: Board instance (should support is_valid_move and check_winner)
        Returns:
            Tuple of (row, col) for AI move, or None if no move possible
        """
        # Try to win this move
        move = self._find_immediate_win(board, self.symbol)
        if move:
            return move
        # Try to block the opponent from winning
        move = self._find_immediate_win(board, self.opponent_symbol)
        if move:
            return move
        # Otherwise, random selection
        return self._random_move(board)

    def _find_immediate_win(self, board, symbol: str) -> Optional[Tuple[int, int]]:
        """
        Scan every available cell: Temporarily play 'symbol'.
        If it results in a win in that cell, return that move.

        Args:
            board: Board instance
            symbol (str): Which player's win to check
        Returns:
            (row, col) tuple if a move is found, else None
        """
        for row in range(3):
            for col in range(3):
                if board.is_valid_move(row, col):
                    # Try the move
                    board.grid[row][col] = symbol
                    is_win = board.check_winner(symbol)
                    board.grid[row][col] = ' '  # Undo move
                    if is_win:
                        return (row, col)
        return None

    def _random_move(self, board) -> Optional[Tuple[int, int]]:
        """
        Get a list of all valid moves and pick one at random.
        Returns None if there are no valid moves left.
        """
        empty = [
            (r, c) for r in range(3) for c in range(3) if board.is_valid_move(r, c)
        ]
        if not empty:
            return None
        return random.choice(empty)
