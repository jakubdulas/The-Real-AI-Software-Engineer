"""
board.py
Defines the Board class for Tic Tac Toe state holding, move validation, and display routines.

Modularity: Board exposes essential mutation, display, and query methods but does no I/O or player logic.
Easily adaptable for different board sizes or winning conditions.
"""

class Board:
    """
    Holds and displays the state of a 3x3 Tic Tac Toe board.
    Provides move validation, win/draw checking, and ASCII board visualization.
    
    For extensibility: generalize row/col size, adapt win logic for other variants, or plug into GUIs.
    """
    def __init__(self):
        # Internal 3x3 grid, storing ' ', 'X', or 'O'. All cells start empty.
        self.grid = [[' ' for _ in range(3)] for _ in range(3)]

    def display(self):
        """
        Prints the current grid in classic ASCII art form.
        Extension: replace with callback for GUI/test.
        """
        print("\n  1   2   3")
        for idx, row in enumerate(self.grid):
            row_letter = chr(ord('A') + idx)
            print(f"{row_letter}  {row[0]} | {row[1]} | {row[2]}")
            if idx != 2:
                print("  ---+---+---")
        print("")

    def place_marker(self, row: int, col: int, marker: str) -> bool:
        """
        Try to place marker at given (row, col). Only empty cells are valid.
        Args:
            row (int): Row index (0-2).
            col (int): Column index (0-2).
            marker (str): 'X' or 'O'.
        Returns:
            bool: True if successful, False if cell is occupied.
        """
        if self.grid[row][col] == ' ':
            self.grid[row][col] = marker
            return True
        return False

    def get_available_moves(self):
        """
        Compute all open cell positions.
        Returns:
            list[(int,int)]: Zero-based row,col tuples for all open cells.
        """
        return [
            (r, c)
            for r in range(3) for c in range(3)
            if self.grid[r][c] == ' '
        ]

    def check_winner(self):
        """
        Check for three-in-a-row winner in rows, columns, or diagonals.
        Returns:
            str or None: Winning symbol ('X'/'O') or None if no winner.
        For extensibility: Generalize for 4x4+ boards, custom win conditions.
        """
        lines = []
        # Rows and columns
        for i in range(3):
            lines.append(self.grid[i])  # rows
            lines.append([self.grid[0][i], self.grid[1][i], self.grid[2][i]])  # columns
        # Diagonals
        lines.append([self.grid[0][0], self.grid[1][1], self.grid[2][2]])
        lines.append([self.grid[0][2], self.grid[1][1], self.grid[2][0]])

        for line in lines:
            if line[0] != ' ' and line.count(line[0]) == 3:
                return line[0]
        return None

    def is_full(self):
        """
        Returns True if all cells are filled (draw condition); else False.
        """
        for row in self.grid:
            if ' ' in row:
                return False
        return True
