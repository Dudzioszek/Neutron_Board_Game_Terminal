from player import Player
import pytest
import random

@pytest.fixture
def board():
    from board import NeutronBoard
    return NeutronBoard()

def test_make_move_human(board, monkeypatch):
    # Set up the test by patching the built-in input function
    # to return a predetermined string when called
    def mock_input(prompt):
        return '4 0 up'
    monkeypatch.setattr('builtins.input', mock_input)

    # Create a player with a human strategy 
    player = Player(board, 'N', 'human')

    # Call the make_move method and assert that it returns True
    # indicating that the move was successful
    assert player.make_move() == True
    assert board.board[1][0] == 'N'

def test_make_move_random(board, monkeypatch):
    # Create a player with the 'random' strategy
    player = Player(board, 'P', 'random')

    # Monkeypatch the random.randint function to always return 0
    def mock_randint(a, b):
        return 0
    monkeypatch.setattr(random, 'randint', mock_randint)

    # Monkeypatch the random.choice function to always return 'up'
    def mock_choice(lst):
        return 'down'
    monkeypatch.setattr(random, 'choice', mock_choice)

    assert player.make_move() == True
    assert board.board[3][0] == 'P'

def test_make_move_smart(board):
    # Set up the player with the smart strategy
    player = Player(board, 'P', 'smart')

    # Set up the board in a specific configuration to test the smart strategy
    board.board = [['P', ' ', ' ', ' ', 'N'],
                   [' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', 'O', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' '],
                   ['N', 'N', 'N', 'N', 'N']]

    # Set the expected move
    expected_move = (0, 0, 'down')

    # Make the move
    player.make_move()

    # Check that the move was made correctly
    assert board.board[expected_move[0]][expected_move[1]] == ' '
    assert board.board[expected_move[0]+1][expected_move[1]] == ' '


def test_make_move_smart_blocked(board):
    # Set up the player with the smart strategy
    player = Player(board, 'P', 'smart')

    # Set up the board in a configuration where the piece is blocked on all sides
    board.board = [['P', 'N', 'N', 'N', 'N'],
                   ['N', 'N', ' ', 'N', 'N'],
                   ['N', ' ', 'O', ' ', 'N'],
                   ['N', 'N', ' ', 'N', 'N'],
                   ['N', 'N', 'N', 'N', 'N']]

    # Make the move
    player.make_move()

    # Check that the move was not made (i.e. the board configuration remains unchanged)
    assert board.board == [['P', 'N', 'N', 'N', 'N'],
                           ['N', 'N', ' ', 'N', 'N'],
                           ['N', ' ', 'O', ' ', 'N'],
                           ['N', 'N', ' ', 'N', 'N'],
                           ['N', 'N', 'N', 'N', 'N']]


def test_make_neutron_move_human(board, monkeypatch):
    # Set up the test by patching the built-in input function
    # to return a predetermined string when called
    def mock_input(prompt):
        return 'up'
    monkeypatch.setattr('builtins.input', mock_input)

    # Create a player with a human strategy 
    player = Player(board, 'N', 'human')

    # Call the make_neutron_move method and assert that it returns True
    # indicating that the move was successful
    assert player.make_neutron_move() == True
    assert board.board[2][0] == ' '
    assert board.board[1][2] == 'O'




def test_move_neutron_random(board, monkeypatch):
    # replace random.choice with a mock that always returns 'up'
    monkeypatch.setattr(random, 'choice', lambda x: 'up')
    player = Player(board, 'P', 'random')
    assert player.make_neutron_move() == True
    assert board.board[0][2] == ' '
    assert board.board[1][2] == 'O'




def test_move_neutron_random(board, monkeypatch):
    # replace random.choice with a mock that always returns 'up'
    monkeypatch.setattr(random, 'choice', lambda x: 'right')
    player = Player(board, 'P', 'random')
    assert player.make_neutron_move() == True
    assert board.board[2][0] == ' '
    assert board.board[2][4] == 'O'


