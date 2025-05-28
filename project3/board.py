class Board:
    """
    Represents a Tic Tac Toe board.
    Manages the board state, printing, and move validation.
    """
    def __init__(self, size=3):
        """Initializes an empty board of given size (default 3x3)."""
        self.size = size
        self.grid = [[' ' for _ in range(size)] for _ in range(size)]

    def print_board(self):
        """Displays the board using ASCII art."""
        for i in range(self.size):
            row = ' | '.join(self.grid[i])
            print(f" {row} ")
            if i < self.size - 1:
                print('-' * (self.size * 4 - 3))

    def is_valid_move(self, row, col):
        """
        Checks if the move at the given (row, col) is valid (cell is empty and within bounds).
        Args:
            row (int): Row index (0-based)
            col (int): Col index (0-based)
        Returns:
            bool: True if move is valid, False otherwise.
        """
        if 0 <= row < self.size and 0 <= col < self.size:
            return self.grid[row][col] == ' '
        return False

    def is_cell_empty(self, row, col):
        """
        Checks if a particular cell is empty (for compatibility with Player input validation).
        """
        if 0 <= row < self.size and 0 <= col < self.size:
            return self.grid[row][col] == ' '
        return False

    def check_winner(self):
        """
        Checks if there is a winner or a tie.
        Returns:
            symbol (str): 'X' or 'O' if someone won, 'Tie' if it's a draw, None otherwise.
        """
        # Check rows and columns
        for i in range(self.size):
            if self.grid[i][0] != ' ' and all(self.grid[i][j] == self.grid[i][0] for j in range(self.size)):
                return self.grid[i][0]
            if self.grid[0][i] != ' ' and all(self.grid[j][i] == self.grid[0][i] for j in range(self.size)):
                return self.grid[0][i]

        # Check diagonals
        if self.grid[0][0] != ' ' and all(self.grid[i][i] == self.grid[0][0] for i in range(self.size)):
            return self.grid[0][0]
        if self.grid[0][self.size-1] != ' ' and all(self.grid[i][self.size-1-i] == self.grid[0][self.size-1] for i in range(self.size)):
            return self.grid[0][self.size-1]

        # Check for tie (if all cells are filled)
        if all(self.grid[row][col] != ' ' for row in range(self.size) for col in range(self.size)):
            return 'Tie'

        # No winner or tie
        return None

    def make_and_show_move(self, row, col, symbol):
        """
        Places a move and immediately prints the updated board.
        Args:
            row (int): Row index (0-based)
            col (int): Column index (0-based)
            symbol (str): Player's symbol ('X' or 'O')
        Returns:
            bool: True if move was successful, False otherwise.
        """
        if self.place_move(row, col, symbol):
            self.print_board()
            return True
        else:
            print("Invalid move! Try again.")
            return False

    def place_move(self, row, col, symbol):
        """
        Places a move on the board at (row, col) for the given symbol (e.g., 'X' or 'O').
        Args:
            row (int)
            col (int)
            symbol (str): Player's symbol
        Returns:
            bool: True if move was placed, False if invalid.
        """
        if self.is_valid_move(row, col):
            self.grid[row][col] = symbol
            return True
        return False
