from board import Board
from player import Player
from ai import TicTacToeAI

class Game:
    """
    Main Game controller for Tic Tac Toe.

    - Handles game mode selection and setup (2-player or vs AI)
    - Controls game flow: board display, move input, updating, win/draw detection
    - Integrates Player, Board, and AI modules
    - Designed for easy extension
    """
    def __init__(self):
        # Main board
        self.board = Board()
        # Players
        self.player1 = None  # Will be set in setup_players()
        self.player2 = None
        self.current_player = None
        # AI module (only if playing vs AI)
        self.ai = None

    def setup_players(self):
        """
        Prompts user to select game mode and creates Player/AI as needed.
        Human can choose symbol (X goes first).
        """
        print("Welcome to Terminal Tic Tac Toe!\n")
        print("Select a game mode:")
        print("1. Two Player (Human vs Human)")
        print("2. Single Player (Human vs AI)")
        while True:
            mode = input("Enter 1 or 2: ").strip()
            if mode not in ["1", "2"]:
                print("Invalid choice. Please enter 1 or 2.")
                continue
            break
        if mode == "1":
            # Two Human Players
            name1 = input("Enter Player 1's name: ").strip() or "Player 1"
            name2 = input("Enter Player 2's name: ").strip() or "Player 2"
            self.player1 = Player(name1, 'X', is_ai=False)
            self.player2 = Player(name2, 'O', is_ai=False)
            self.ai = None
        else:
            # Human vs AI: user chooses X or O
            name1 = input("Enter your name: ").strip() or "You"
            while True:
                human_symbol = input("Do you want to be X or O? (X goes first): ").strip().upper()
                if human_symbol not in ["X", "O"]:
                    print("Please enter X or O.")
                    continue
                break
            ai_symbol = 'O' if human_symbol == 'X' else 'X'
            self.player1 = Player(name1, human_symbol, is_ai=False)
            self.player2 = Player("AI", ai_symbol, is_ai=True)
            # Set "ai" attribute to whichever player is the AI (always one of them)
            self.ai = TicTacToeAI(self.player2.symbol)
            if self.player1.symbol == 'O':
                # Human chose O, so AI is X and goes first
                # Make AI always self.player2 regardless, but AI will actually start first
                pass
        self.current_player = self.player1  # X always starts (per setup above)

    def switch_turn(self):
        """
        Switch current player to the other player (toggle turns).
        """
        self.current_player = (
            self.player2 if self.current_player == self.player1 else self.player1
        )

    def prompt_move(self):
        """
        Prompts the current player (human or AI) to choose their move.
        For human: validates and parses numeric input until valid.
        For AI: invokes TicTacToeAI and displays AI's choice.
        Returns:
            (row, col): tuple as zero-based indices
        """
        if not self.current_player.is_ai:
            # Human move - keep prompting until 100% valid
            while True:
                try:
                    move = input(f"{self.current_player.name} ({self.current_player.symbol}), enter your move (row col from 1-3): ")
                    row, col = map(int, move.split())
                    row_idx, col_idx = row - 1, col - 1
                    if not (0 <= row_idx < 3 and 0 <= col_idx < 3):
                        print("Row and column must be in the range 1-3.")
                        continue
                    if not self.board.is_valid_move(row_idx, col_idx):
                        print("That cell is already occupied. Try again.")
                        continue
                    return (row_idx, col_idx)
                except ValueError:
                    print("Invalid input. Please enter two numbers (1-3) separated by a space.")
        else:
            # AI chooses move
            print(f"{self.current_player.name} ({self.current_player.symbol}) is thinking...")
            move = self.ai.select_move(self.board)
            if move:
                print(f"AI selects row {move[0]+1}, column {move[1]+1}")
            else:
                print("AI could not select a move! (This should not happen.)")
            return move

    def check_winner(self):
        """
        Checks if the current player has won the game.
        Returns:
            bool: True if the current player has won
        """
        return self.board.check_winner(self.current_player.symbol)

    def check_draw(self):
        """
        Checks if the game has ended in a draw (full board, no winner).
        Returns:
            bool: True if the board is full and no winner
        """
        return self.board.is_full() and not self.board.check_winner('X') and not self.board.check_winner('O')

    def play(self):
        """
        Start and play a single game of Tic Tac Toe.
        Runs the game loop, prompts players, handles moves,
        and announces win/draw/game over states.
        """
        self.setup_players()
        self.board.reset()
        while True:
            self.board.display()
            row, col = self.prompt_move()
            self.board.update_cell(row, col, self.current_player.symbol)
            if self.check_winner():
                self.board.display()
                print(f"{self.current_player.name} ({self.current_player.symbol}) wins!\n")
                break
            if self.check_draw():
                self.board.display()
                print("It's a draw!\n")
                break
            self.switch_turn()
        print("Game over.")


def main():
    """
    Entry point: allows for repeated play until the user quits.
    """
    game = Game()
    while True:
        game.play()
        retry = input("Play again? (y/n): ").strip().lower()
        if retry != 'y':
            print("Thanks for playing Tic Tac Toe!")
            break

if __name__ == '__main__':
    main()
