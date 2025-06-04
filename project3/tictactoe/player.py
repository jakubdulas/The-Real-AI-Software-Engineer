"""
Player module for Tic Tac Toe
Provides the Player class to represent human and AI players.
"""

class Player:
    """
    Represents a player in the Tic Tac Toe game. Stores name, symbol, and AI status.
    """

    def __init__(self, name: str, symbol: str, is_ai: bool = False):
        """
        Initialize a Player instance.
        Args:
            name (str): User-facing name or identifier of the player.
            symbol (str): Player's symbol, usually 'X' or 'O'.
            is_ai (bool): If True, this player will act as an AI.
        """
        self.name = name
        self.symbol = symbol
        self.is_ai = is_ai

    def __str__(self):
        """
        Human readable player representation for prompts and debugging.
        """
        type_desc = "AI" if self.is_ai else "Human"
        return f"{self.name} ({self.symbol}) - {type_desc}"
