"""
ai.py
Defines AIPlayer—the artificial intelligence opponent for Tic Tac Toe.
AIPlayer's logic is modular: extend or subclass for better strategies (minimax, heuristics, etc).
"""

import random
from typing import Tuple, List

class AIPlayer:
    """
    Basic AI player for Tic Tac Toe.
    Chooses a random move among available board cells.
    
    To extend: override get_move with more sophisticated algorithms
    (minimax, heuristics, lookup tables, etc.).
    """
    def __init__(self, symbol: str, name: str = 'AI'):
        """
        Args:
            symbol (str): The marker ('X' or 'O') used by this player.
            name (str): Player display name (default: 'AI').
        """
        self.symbol = symbol
        self.name = name

    def __str__(self):
        return f"{self.name} ({self.symbol})"

    def get_move(self, board) -> Tuple[int, int]:
        """
        Select a legal move given the current board state.
        Args:
            board (Board): Board exposing get_available_moves().
        Returns:
            (int, int): Tuple of row, col indices for move.
        Raises:
            RuntimeError: If called with no available moves (should not happen).
        Extension point: Replace with AI logic for strategic moves.
        """
        available_moves: List[Tuple[int, int]] = board.get_available_moves()
        if not available_moves:
            raise RuntimeError('No moves available for AI.')
        print(f"{self} (AI) is thinking...")
        return random.choice(available_moves)
