from player import Player
from board import Board
from ai import GameAI

def main():
    print("Welcome to Tic Tac Toe!")
    mode = input("Choose mode: 1 (Human vs Human), 2 (Human vs AI): ").strip()
    name1 = input("Enter the name for Player 1 (X): ").strip() or "Player 1"
    if mode == '2':
        name2 = "AI Bot"
        player1 = Player(name1, 'X')
        player2 = GameAI(name2, 'O')
    else:
        name2 = input("Enter the name for Player 2 (O): ").strip() or "Player 2"
        player1 = Player(name1, 'X')
        player2 = Player(name2, 'O')

    board = Board()
    current_player = player1

    board.print_board()

    while True:
        if isinstance(current_player, GameAI):
            print(f"{current_player.name} ({current_player.marker}) is thinking...")
        move = current_player.get_move(board)

        if move is None:
            print("No valid moves left!")
            break
        row, col = move

        # Place the move with correct symbol/marker
        symbol = current_player.marker if hasattr(current_player, "marker") else current_player.symbol
        board.place_move(row, col, symbol)
        board.print_board()

        result = board.check_winner()
        if result == 'X':
            print(f"{player1.name} wins! Congratulations!")
            break
        elif result == 'O':
            print(f"{player2.name} wins! Congratulations!")
            break
        elif result == 'Tie':
            print("It's a tie!")
            break
        # Switch players
        current_player = player2 if current_player == player1 else player1

if __name__ == "__main__":
    main()
