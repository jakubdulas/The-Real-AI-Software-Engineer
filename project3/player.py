class Player:
    """
    Represents a human player in Tic Tac Toe.
    Handles player name assignment and input/move submission.
    """
    def __init__(self, name: str, symbol: str):
        """
        Initialize a Player with a name and playing symbol (X or O).
        """
        self.name = name
        self.symbol = symbol

    def get_move(self, board):
        """
        Prompt the player to enter their move.
        
        Args:
            board: The Board object for validation.
        Returns:
            (row, col): Tuple of integers indicating the move.
        """
        while True:
            try:
                move = input(f"{self.name} ({self.symbol}), enter your move as row,col (e.g. 1,3): ").strip()
                if ',' not in move:
                    print("Invalid format. Please use row,col (e.g. 1,3).")
                    continue
                row_str, col_str = move.split(',')
                row, col = int(row_str) - 1, int(col_str) - 1
                if row not in range(3) or col not in range(3):
                    print("Row and column must be between 1 and 3.")
                    continue
                if not (hasattr(board, 'is_cell_empty') and board.is_cell_empty(row, col)):
                    # Fallback to is_valid_move for compatibility
                    if not board.is_valid_move(row, col):
                        print("Cell is already occupied or move invalid. Choose another one.")
                        continue
                return row, col
            except ValueError:
                print("Invalid input. Please enter numbers for row and column.")
