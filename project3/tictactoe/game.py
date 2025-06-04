"""
game.py
Defines the Game class, responsible for managing the main gameplay loop, player turns,
and game-over detection for both human and AI opponents.

Separation of concerns:
- Game orchestrates player turns, win/draw logic, and interacts with Board and Player subclasses.
- No direct I/O except for board/game messages—adapting for GUI or network play is straightforward.
- Easily extensible (custom AI/Player strategies, custom end conditions, etc).
"""

from .player import Player
from .board import Board
from .ai import AIPlayer

class Game:
    """
    Controller for a Tic Tac Toe match between two players (human or AI).
    Handles turns, move input requests, win/draw detection, and message display.
    
    To extend: subclass Game for custom rules, override play(), or add hooks for event notifications.
    """
    def __init__(self, player1, player2):
        """
        Args:
            player1 (Player): First player (starts first, 'X').
            player2 (Player): Second player ('O').
        """
        self.board = Board()
        self.players = [player1, player2]
        self.current_turn = 0  # Whose turn: 0 = player1, 1 = player2

    def switch_turn(self):
        """
        Switch the internal turn index. Allows seamless two-player alternation.
        """
        self.current_turn = 1 - self.current_turn

    def play(self):
        """
        Main game loop: handles alternate player turns (human or AI), board display, move requests,
        input validation, win/draw detection, and output of results.
        
        Future extensions: plug in event handlers, callbacks, GUI display hooks, or alternate move strategies.
        """
        print("Welcome to Tic Tac Toe!\n")
        while True:
            self.board.display()
            current_player = self.players[self.current_turn]
            print(f"{current_player}'s turn.")
            # Unified move interface lets both Human and AI participate transparently
            row, col = current_player.get_move(self.board)
            moved = self.board.place_marker(row, col, current_player.symbol)
            if not moved:
                print("Invalid move. Try again!\n")
                continue
            winner_marker = self.board.check_winner()
            if winner_marker:
                self.board.display()
                # The player who just moved is always the winner when detected
                print(f"Congratulations! {current_player} wins!")
                break
            elif self.board.is_full():
                self.board.display()
                print("It's a draw!")
                break
            self.switch_turn()
