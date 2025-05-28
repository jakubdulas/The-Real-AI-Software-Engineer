from board import Board
from player import Player
from ai_player import AIPlayer

class Game:
    """
    The Game class manages the lifecycle and logic of a Tic Tac Toe game session.
    It allows for two-player or player-vs-AI modes, alternates turns, handles user interaction,
    integrates with the Board and Player classes (including simple AI), and oversees win/draw detection.
    """
    def __init__(self):
        """
        Initializes the Game, including the creation of the Board and Player/AI instances.
        Determines which mode (Human vs. Human or Human vs. AI) to play based on user input.
        """
        self.board = Board()
        self.players = []
        self.current_idx = 0  # Player 1 starts
        self.game_over = False
        self.winner = None
        self.draw = False

        self.select_game_mode()

    def select_game_mode(self):
        """
        Prompt the user to choose a game mode (2 players or 1 vs AI), then initialize players.

        Extensibility notes:
            - To add new types of players (remote/bot/custom AI), extend the AIPlayer class or
              implement a new class with a get_move(board) method like Player and AIPlayer.
            - For more game modes, add options and expand the player initialization logic below.
        """
        print("Welcome to Terminal Tic Tac Toe!")
        print("Select game mode:")
        print("1. Human vs Human")
        print("2. Human vs AI")
        while True:
            mode = input("Enter 1 or 2: ").strip()
            if mode == "1":
                # Human vs Human mode: Instantiate two Player objects with X and O
                self.players = [
                    Player(name="Player 1", symbol="X"),
                    Player(name="Player 2", symbol="O")
                ]
                print("\n--- Two Player Mode Selected ---\n")
                break
            elif mode == "2":
                # Human vs AI mode: First player is always human (X); second is AI (O)
                # To support different combinations (e.g., AI as X), prompt and modify logic.
                human_name = input("Enter your name: ").strip() or "You"
                symbol = "X"
                self.players = [
                    Player(name=human_name, symbol=symbol),
                    AIPlayer(symbol=("O" if symbol == "X" else "X"), name="AI")
                ]
                print(f"\n--- Human vs AI Mode: {human_name} (X) vs AI (O) ---\n")
                break
            else:
                print("Invalid mode. Please enter 1 or 2.")

    def play(self):
        """
        Run the main loop for the selected game mode (Human vs Human, or Human vs AI).
        Displays the board after each move, obtains moves from Player or AI, and terminates on win or draw.
        """
        self.board.display()
        while not self.game_over:
            current_player = self.players[self.current_idx]
            # Get and validate the next move
            move_valid = False
            while not move_valid:
                try:
                    # For AI, no input needed
                    move = current_player.get_move(self.board)
                except Exception:
                    print("Move input failed, try again.")
                    continue
                if move is None:
                    # No valid moves remaining (AI defensive)
                    print(f"{current_player.name} cannot make a move.")
                    break
                row, col = move
                move_valid = self.board.make_move(row, col, current_player.symbol)
                if not move_valid:
                    print("Cell is occupied or input invalid. Try again.")
            self.board.display()
            # Check for a winner
            if self.board.check_winner(current_player.symbol):
                self.game_over = True
                self.winner = current_player
                print(f"Congratulations, {current_player.name} ({current_player.symbol}) wins!")
                break
            # Check for a draw
            if self.board.is_full():
                self.game_over = True
                self.draw = True
                print("It's a draw!")
                break
            # Switch to the other player
            self.current_idx = 1 - self.current_idx

# Monkey-patch a helper for Player compatibility (required by Player.get_move)
def is_cell_empty(self, row, col):
    """
    Return True if the cell at (row, col) is empty; False if occupied.
    """
    return not self.is_occupied(row, col)
Board.is_cell_empty = is_cell_empty

if __name__ == "__main__":
    game = Game()
    game.play()
