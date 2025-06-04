"""
player.py
Defines the Player class (for human participants).

Future extensibility: Player can be extended with GUI move picking, network play, etc.
All input is abstracted via get_move().
"""

class Player:
    """
    Represents a (human) Tic Tac Toe player.
    Provides input interface and player identity.
    
    Extension: subclass Player for GUI/network move-picking or input constraints.
    """
    def __init__(self, name: str, symbol: str):
        """
        Args:
            name (str): Player's display name or ID.
            symbol (str): 'X' or 'O'.
        """
        self.name = name
        self.symbol = symbol

    def __str__(self):
        return f"{self.name} ({self.symbol})"

    def get_move(self, board):
        """
        Prompt human user for (row, col). Input and validation loops continue until a valid
        move is provided.
        Args:
            board (Board): Current board for move validation.
        Returns:
            (int, int): Chosen (row, col), always zero-based.
        Extension: Override for new UX (GUI, file input, online play).
        """
        while True:
            try:
                move = input(f"{self}, enter your move as row and column (e.g., 1 3): ")
                row_str, col_str = move.strip().split()
                row, col = int(row_str) - 1, int(col_str) - 1
                if 0 <= row < 3 and 0 <= col < 3:
                    if board.grid[row][col] == ' ':
                        return row, col
                    else:
                        print("That cell is already taken.")
                else:
                    print("Coordinates must be between 1 and 3.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter row and column as two numbers (e.g., 1 3).")
