class Board:
    """
    The Board class encapsulates all functionality related to the Tic Tac Toe board.
    Responsibilities include:
      - Maintaining the internal game board state
      - Displaying the current board state in an ASCII art format
      - Validating moves and board positions
      - Recording player moves
      - Checking win and draw conditions
      - Utility functions to support game logic and extensibility
    """

    BOARD_SIZE = 3
    EMPTY_CELL = ' '

    def __init__(self):
        """
        Initialize an empty 3x3 Tic Tac Toe board.
        """
        self.grid = [[self.EMPTY_CELL for _ in range(self.BOARD_SIZE)] for _ in range(self.BOARD_SIZE)]

    def display(self):
        """
        Print the board to the terminal in a user-friendly ASCII format with row/column numbers.
        """
        print('\n  1   2   3')
        for idx, row in enumerate(self.grid):
            print(f"{idx+1} " + " | ".join(row))
            if idx < self.BOARD_SIZE - 1:
                print("  " + "---+---+---")
        print()

    def is_occupied(self, row, col):
        """
        Check if a specific cell is already taken by a player symbol.
        Args:
            row (int): Row index (0-based).
            col (int): Column index (0-based).
        Returns:
            bool: True if occupied; False otherwise.
        """
        return self.grid[row][col] != self.EMPTY_CELL

    def is_cell_empty(self, row, col):
        """
        Check if a board cell is both inside bounds and currently empty.
        Args:
            row (int): Row index (0-based).
            col (int): Column index (0-based).
        Returns:
            bool: True if within bounds and not occupied; False otherwise.
        """
        return self.is_valid_position(row, col) and not self.is_occupied(row, col)

    def make_move(self, row, col, symbol):
        """
        Place a symbol ('X' or 'O') in the specified cell if it is a valid move.
        Args:
            row (int): Row index (0-based).
            col (int): Column index (0-based).
            symbol (str): The player's symbol.
        Returns:
            bool: True if move succeeds; False otherwise (e.g., cell is occupied).
        """
        if self.is_valid_position(row, col) and not self.is_occupied(row, col):
            self.grid[row][col] = symbol
            return True
        return False

    def is_valid_position(self, row, col):
        """
        Determine if (row, col) is within the 3x3 board boundaries.
        Args:
            row (int): Row index (0-based).
            col (int): Column index (0-based).
        Returns:
            bool: True if within bounds; otherwise False.
        """
        return 0 <= row < self.BOARD_SIZE and 0 <= col < self.BOARD_SIZE

    def reset(self):
        """
        Clear the board, resetting all cells to empty. Use to restart a game.
        """
        self.grid = [[self.EMPTY_CELL for _ in range(self.BOARD_SIZE)] for _ in range(self.BOARD_SIZE)]

    def get_empty_positions(self):
        """
        Return a list of all empty cells as (row, col) tuples.
        Returns:
            list: List of unoccupied cell coordinates.
        """
        empty = []
        for row in range(self.BOARD_SIZE):
            for col in range(self.BOARD_SIZE):
                if not self.is_occupied(row, col):
                    empty.append((row, col))
        return empty

    def check_winner(self, symbol):
        """
        Check whether the specified symbol has achieved a win (3 in a row, column, or diagonal).
        Args:
            symbol (str): The symbol to check for ('X' or 'O').
        Returns:
            bool: True if the symbol has a winning line; otherwise False.
        """
        # Check rows
        for row in self.grid:
            if all(cell == symbol for cell in row):
                return True

        # Check columns
        for col in range(self.BOARD_SIZE):
            if all(self.grid[row][col] == symbol for row in range(self.BOARD_SIZE)):
                return True

        # Check main diagonal
        if all(self.grid[i][i] == symbol for i in range(self.BOARD_SIZE)):
            return True
        # Check anti-diagonal
        if all(self.grid[i][self.BOARD_SIZE - 1 - i] == symbol for i in range(self.BOARD_SIZE)):
            return True
        return False

    def is_full(self):
        """
        Return True if there are no empty spaces left on the board (draw condition).
        Returns:
            bool: True if board is completely filled; otherwise False.
        """
        return all(
            self.grid[row][col] != self.EMPTY_CELL
            for row in range(self.BOARD_SIZE)
            for col in range(self.BOARD_SIZE)
        )
