import random

class GameAI:
    """
    Simple AI player for Tic Tac Toe. Chooses a random legal move.
    """
    def __init__(self, name, marker):
        self.name = name
        self.marker = marker

    def get_move(self, board):
        """
        Select a random valid move from the available spaces on the board.
        Args:
            board: The Board object instance where moves will be made
        Returns:
            Tuple (row, col) for next move
        """
        available_moves = []
        for row in range(3):
            for col in range(3):
                if board.is_valid_move(row, col):
                    available_moves.append((row, col))
        if not available_moves:
            return None  # No moves left (draw)
        return random.choice(available_moves)
