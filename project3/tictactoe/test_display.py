from board import Board

def test_board_display():
    board = Board()
    print("Initial board:")
    board.display()

    # X makes a move at (0, 0)
    board.place_marker(0, 0, 'X')
    print("After X moves to A1:")
    board.display()

    # O makes a move at (1, 1)
    board.place_marker(1, 1, 'O')
    print("After O moves to B2:")
    board.display()

    # Fill board for draw scenario
    fill_moves = [
        (0, 1, 'X'), (0, 2, 'O'),
        (1, 0, 'X'), (1, 2, 'O'),
        (2, 0, 'O'), (2, 1, 'X'), (2, 2, 'X')
    ]
    for row, col, marker in fill_moves:
        board.place_marker(row, col, marker)
    print("Filled board (simulate draw):")
    board.display()

if __name__ == "__main__":
    test_board_display()
