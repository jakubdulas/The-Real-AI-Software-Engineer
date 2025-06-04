import io
import sys
import builtins
from unittest import mock
import pytest

from tictactoe.main import main


def run_main_with_inputs(inputs):
    """ Helper to run main() with the provided input sequence and capture printed output. """
    input_iter = iter(inputs)
    with mock.patch('builtins.input', lambda _: next(input_iter)):
        with mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            try:
                main()
            except StopIteration:
                # Not enough inputs provided, usually a test issue
                pass
            output = fake_stdout.getvalue()
    return output

def test_player_x_wins():
    # Scenario: Player X wins by completing the top row
    moves = [
        'Alice',    # Player 1 name
        'Bob',      # Player 2 name
        '1 1',      # Alice X - (0,0)
        '1 2',      # Bob O   - (0,1)
        '2 1',      # Alice X - (1,0)
        '2 2',      # Bob O   - (1,1)
        '3 1'       # Alice X - (2,0) --> win
    ]
    output = run_main_with_inputs(moves)
    assert 'Alice (X) wins!' in output
    assert 'Game Over' in output
    # Board should show X in first col of each row
    assert '\nX |' in output

def test_draw_game():
    # Scenario: Full board, no winner
    moves = [
        'Alice', 'Bob',
        '1 1',  # X
        '1 2',  # O
        '1 3',  # X
        '2 1',  # O
        '2 3',  # X
        '2 2',  # O
        '3 1',  # X
        '3 3',  # O
        '3 2'   # X (last move - draw)
    ]
    output = run_main_with_inputs(moves)
    assert 'It\'s a draw!' in output
    assert 'Game Over' in output

def test_invalid_and_repeated_input():
    # Tries an invalid cell (out of bounds), then an occupied cell, then a valid move
    moves = [
        'Alice', 'Bob',
        '0 0',    # Invalid input (outside board)
        '1 1',    # Alice: valid
        '1 1',    # Bob: occupied cell
        '1 2',    # Bob: valid
        '2 1',    # Alice: valid
        '2 2',    # Bob: valid
        '3 1',    # Alice: valid (no winner in this sequence)
        '1 3',    # Bob: valid
        '2 3',    # Alice: valid
        '3 2',    # Bob: valid
        '3 3'     # Alice: valid, fills board
    ]
    output = run_main_with_inputs(moves)
    assert 'Cell already taken' in output
    assert 'Invalid input' in output or 'Row/Column must be between' in output
    assert ('wins!' in output) or ("It's a draw!" in output)

if __name__ == '__main__':
    pytest.main([__file__])
