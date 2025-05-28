import random

class AIPlayer:
    """
    AIPlayer represents a simple AI for Tic Tac Toe that selects moves automatically.
    
    The current strategy is to choose a random empty cell from the board. This class is designed
    to be easily extended with more advanced AI logic, such as minimax or heuristics.
    
    Usage:
        ai = AIPlayer(symbol='O')
        move = ai.get_move(board)  # Returns (row, col)
    
    Extensibility notes:
        - To implement a stronger AI, replace or extend the logic in get_move (e.g., minimax).
        - You can add a difficulty setting by passing an additional argument to __init__, then
          branching logic in get_move accordingly.
        - To add other types of programmatic players (e.g., remote, heuristic), subclass this IAPlayer
          or follow this interface (symbol, name, get_move(board)).
    """
    def __init__(self, symbol, name="AI"):
        """
        Initialize the AI player.

        Args:
            symbol (str): The symbol ('X' or 'O') that the AI uses.
            name (str): The name of the AI player (default: "AI").
        """
        self.symbol = symbol
        self.name = name

    def get_move(self, board):
        """
        Select a move for the AI by choosing a random empty cell.
        
        Args:
            board (Board): The current state of the board.

        Returns:
            tuple: (row, col) indices for the move, or None if no moves left.
        
        Extensibility note:
            To improve the AI, replace the random selection with a strategy:
            - Example: Implement Minimax for unbeatable AI.
            - Example: Add prioritization for center or corners.
        """
        # List all empty cells among the 3x3 board.
        empty_cells = [
            (row, col)
            for row in range(3)
            for col in range(3)
            if board.is_cell_empty(row, col)
        ]
        if not empty_cells:
            return None  # No available moves
        # Randomly select one of the empty cells for the move.
        return random.choice(empty_cells)
