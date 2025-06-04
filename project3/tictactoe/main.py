"""
main.py
Entrypoint for running the Tic Tac Toe game.

This script initializes the game, gathers user preferences (human vs AI),
assembles the correct player objects, and starts gameplay. For extensibility,
game setup and launch logic are deliberately separated from the game logic itself.
"""

from tictactoe.player import Player
from tictactoe.game import Game
from tictactoe.ai import AIPlayer

def prompt_game_mode():
    """
    Prompt the user to choose between Human vs Human and Human vs AI modes.
    Returns:
        str: "1" for Human vs Human, "2" for Human vs AI.
    """
    print("Tic Tac Toe Game\n")
    mode = ""
    while mode not in {"1", "2"}:
        print("Choose a game mode:")
        print("1. Human vs Human")
        print("2. Human vs AI")
        mode = input("Enter 1 or 2: ").strip()
    return mode

def main():
    """
    Collect player names, create Player/AIPlayer instances,
    and launch the game loop. This main launcher is isolated from game logic
    so GUI or network versions can directly reuse or wrap it.
    """
    mode = prompt_game_mode()
    name1 = input("Enter Player 1 name (X): ").strip() or "Player 1"
    player1 = Player(name1, "X")
    if mode == "1":
        name2 = input("Enter Player 2 name (O): ").strip() or "Player 2"
        player2 = Player(name2, "O")
    else:
        name2 = input("Enter AI name (or leave blank for 'AI'): ").strip() or "AI"
        player2 = AIPlayer("O", name=name2)
    print("")
    game = Game(player1, player2)
    game.play()

if __name__ == "__main__":
    main()
