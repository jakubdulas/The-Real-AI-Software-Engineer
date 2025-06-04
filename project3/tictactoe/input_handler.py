"""
input_handler.py
Utility for centralized input validation and parsing.

For extensibility: plug in alternate input functions for GUI, file, or network play.
Keep user messaging and input validation logic outside core game logic.
"""

def get_valid_move(player_name, board):
    """
    Request a move from the player, providing full input validation and cell vacancy checks.
    
    Args:
        player_name (str): Display name of player for prompt.
        board (Board): The active Board instance (must expose .grid and .size).
    Returns:
        (int, int): (row, col) indices (zero-based), always a legal move.
    For extensibility: Override this in GUIs or to add custom move prompts.
    """
    board_size = getattr(board, 'size', 3)  # Hardcoded fallback for legacy boards
    while True:
        try:
            move = input(f"{player_name}, enter your move as row and column (e.g., 1 2): ").strip()
            if not move:
                print("Input cannot be empty. Try again.")
                continue
            row_col = move.split()
            if len(row_col) != 2:
                print("Please enter two numbers separated by a space (e.g., 1 3).")
                continue
            row, col = int(row_col[0])-1, int(row_col[1])-1  # User enters 1-based index
            if (row < 0 or row >= board_size or col < 0 or col >= board_size):
                print(f"Invalid position: Input must be between 1 and {board_size} for both row and column.")
                continue
            if board.grid[row][col] != ' ':
                print("Cell already occupied. Please choose a different cell.")
                continue
            return (row, col)
        except ValueError:
            print("Invalid input. Please enter numbers only (e.g., 2 3). Try again.")
