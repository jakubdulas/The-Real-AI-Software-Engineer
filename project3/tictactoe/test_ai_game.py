"""
test_ai_game.py
Integration and unit tests for Human vs AI Tic Tac Toe flow and AIPlayer behaviors.

Purpose: Ensure main loop integration (mode prompt, correct player setup, AI move validity),
and document correct interface for future test extension as AI is enhanced or replaced.
"""

import builtins
from unittest.mock import patch
from tictactoe.main import main
from tictactoe.ai import AIPlayer
from tictactoe.board import Board

def test_human_vs_ai_flow(monkeypatch, capsys):
    """
    Integration test for Human (X) vs AI (O).
    Simulates UI, drive game flow, and catches win/draw announcements.
    Future: Extend to cover replay, alternate AI strategies, or GUI replacement.
    """
    inputs = iter([
        '2',          # Choose Human vs AI
        'Tester',     # Player 1 (X)
        '',           # Use 'AI' as default AI name
        '1 1',        # Human X move
        '2 2',        # Human X move
        '3 3',        # Human X move
        '1 2',        # Human X move
    ])

    def mock_input(prompt):
        value = next(inputs)
        print(prompt + value)
        return value

    with patch('builtins.input', mock_input):
        main()

    output = capsys.readouterr().out
    assert "Choose" in output and "AI" in output
    assert 'Congratulations!' in output or "It's a draw!" in output
    # AI move announcement
    assert "AI (O) is thinking" in output or "AI is thinking" in output

def test_ai_move_is_valid():
    """
    Ensure AI picks a legal, unoccupied cell.
    Future: Test alternate AI logic, and other board sizes.
    """
    board = Board()
    board.place_marker(0, 0, 'X')
    board.place_marker(0, 1, 'O')
    ai = AIPlayer('X')
    move = ai.get_move(board)
    assert move in board.get_available_moves()

def test_ai_player_str():
    """
    AI's __str__ is correct.
    """
    ai = AIPlayer('O', name='Bot')
    assert str(ai) == 'Bot (O)'
