class Player:
    """
    Player class represents a human participant in the game of Tic Tac Toe.
    It stores player-specific information and facilitates user interaction
    for move selection with robust input validation.
    """
    def __init__(self, name: str, symbol: str):
        """
        Initialize a new human player with a given name and symbol (X or O).
        Args:
            name (str): Human-readable name for the player.
            symbol (str): Symbol used on the board (should be 'X' or 'O').
        """
        self.name = name
        self.symbol = symbol.upper()

    def get_move(self, board):
        """
        Repeatedly prompt the player for a move until a valid, unoccupied
        board cell (1-based input) is given. Ensures correct format and cell availability.
        Args:
            board (Board): The game board, which must implement is_valid_position and is_cell_empty.
        Returns:
            tuple: (row, col) zero-based tuple indicating the selected cell.
        """
        while True:
            try:
                user_input = input(f"{self.name} ({self.symbol}), enter your move as row,col (e.g., 1,3): ")
                row_str, col_str = user_input.strip().split(",")
                row, col = int(row_str.strip()) - 1, int(col_str.strip()) - 1
                
                if not board.is_valid_position(row, col):
                    print("Coordinates must be from 1 to 3. Please try again.")
                    continue
                
                if not board.is_cell_empty(row, col):
                    print("That cell is already taken. Try again.")
                    continue
                return (row, col)
            except ValueError:
                print("Invalid input format. Enter row,col as two integers (e.g. 2,3). Try again.")
