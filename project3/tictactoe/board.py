"""
Board module for Tic Tac Toe

Defines the Board class and all board-related operations.
"""

class Board:
    """
    Represents the Tic Tac Toe board and its operations.
    Handles state, move updates, display, and win/draw checks.
    """

    def __init__(self):
        """Initialize a blank board (3x3 grid)."""
        self.reset()

    def display(self):
        """
        Display the board in a readable ASCII format for the terminal.
        Also adds row and column numbers for player reference.
        """
        print("\n   1   2   3")
        for idx, row in enumerate(self.grid):
            row_display = f"{idx+1}  " + " | ".join(row)
            print(row_display)
            if idx < 2:
                print("  ---+---+---")
        print()

    def reset(self):
        """
        Reset the board state to the initial empty cells.
        """
        self.grid = [[" " for _ in range(3)] for _ in range(3)]

    def update_cell(self, row, col, symbol):
        """
        Place a symbol ('X' or 'O') in the cell at (row, col) if valid.
        Args:
            row (int): Zero-based row index (0-2)
            col (int): Zero-based column index (0-2)
            symbol (str): 'X' or 'O'
        Returns:
            bool: True if placement successful, else False.
        """
        if self.is_valid_move(row, col):
            self.grid[row][col] = symbol
            return True
        return False

    def is_valid_move(self, row, col):
        """
        Check if the specified cell is empty and indices are in bounds.
        Args:
            row (int): 0, 1, or 2
            col (int): 0, 1, or 2
        Returns:
            bool: True if cell is available for a move
        """
        return 0 <= row < 3 and 0 <= col < 3 and self.grid[row][col] == " "

    def is_cell_occupied(self, row, col):
        """
        Check if a cell at (row, col) is already played.
        Args:
            row (int): row index
            col (int): column index
        Returns:
            bool: True if cell is not empty; otherwise False.
        """
        return self.grid[row][col] != " "

    def check_winner(self, symbol):
        """
        Check if the passed-in symbol ('X' or 'O') has a win on the board.
        Evaluates all rows, columns, and diagonals.
        Args:
            symbol (str): 'X' or 'O'
        Returns:
            bool: True if that symbol has a winning set of three
        """
        # Check each row
        for row in self.grid:
            if all(cell == symbol for cell in row):
                return True
        # Check each column
        for col in range(3):
            if all(self.grid[row][col] == symbol for row in range(3)):
                return True
        # Check diagonals
        if all(self.grid[i][i] == symbol for i in range(3)):
            return True
        if all(self.grid[i][2 - i] == symbol for i in range(3)):
            return True
        return False

    def is_full(self):
        """
        Check if there are no empty spaces left on the board.
        Returns:
            bool: True if the board is full (draw), otherwise False
        """
        for row in self.grid:
            if " " in row:
                return False
        return True
