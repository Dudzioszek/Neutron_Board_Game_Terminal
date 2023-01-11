import pytest


@pytest.fixture
def board():
    from board import NeutronBoard
    board.board =   [['P', 'P', 'P', 'P', 'P'],
                      [' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', 'O', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' '],
                      ['N', 'N', 'N', 'N', 'N']]
    return NeutronBoard()


def test_move_piece_invalid_direction(board, monkeypatch):

    assert board.move_piece(3, 3, 'invalid', 'P') == False


def test_move_piece_invalid_color(board, monkeypatch):

    assert board.move_piece(0, 0, 'right', 'P') == False
    assert board.move_piece(4, 4, 'right', 'N') == False


def test_move_piece_invalid_coordinates(board, monkeypatch):
    
    assert board.move_piece(0, 0, 'right', 'P') == False
    assert board.move_piece(4, 4, 'right', 'N') == False


def test_move_piece_invalid_destination(board, monkeypatch):
    

    assert board.move_piece(1, 2, 'right', 'P') == False


def test_move_piece_valid(board, monkeypatch):

    assert board.move_piece(0, 2, 'down', 'P') == True


def test_move_piece_up(board):
    assert board.move_piece(4, 0, 'up', 'N') == True
    assert board.board[1][0] == 'N'


def test_move_piece_down(board):
    assert board.move_piece(0, 1, 'down', 'P') == True
    assert board.board[3][1] == 'P'


def test_move_piece_left(board):
    board.board = [['P', 'P', 'P', 'P', 'P'],
                   [' ', ' ', ' ', ' ', ' '],
                   ['O', ' ', ' ', ' ', 'N'],
                   [' ', ' ', ' ', ' ', ' '],
                   ['N', 'N', 'N', 'N', ' ']]
    assert board.move_piece(2, 4, 'left', 'N') == True
    assert board.board[2][1] == 'N'


def test_move_piece_right(board):
    board.board = [['P', 'P', 'P', ' ', ' '],
                   ['O', ' ', ' ', ' ', ' '],
                   ['N', ' ', ' ', 'P', 'P'],
                   [' ', ' ', ' ', ' ', ' '],
                   [' ', 'N', 'N', 'N', 'N']]
    assert board.move_piece(2, 0, 'right', 'N') == True
    assert board.board[2][2] == 'N'


def test_move_piece_up_right(board):
    board.board = [['P', 'P', 'P', 'P', 'P'],
                   [' ', ' ', ' ', ' ', ' '],
                   ['O', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' '],
                   ['N', 'N', 'N', 'N', 'N']]
    assert board.move_piece(4, 0, 'up-right', 'N') == True
    assert board.board[1][3] == 'N'


def test_move_piece_up_left(board):
    board.board = [['P', 'P', 'P', 'P', 'P'],
                   [' ', ' ', ' ', ' ', ' '],
                   ['O', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' '],
                   ['N', 'N', 'N', 'N', 'N']]
    assert board.move_piece(4, 4, 'up-left', 'N') == True
    assert board.board[1][1] == 'N'


def test_move_piece_down_right(board):
    board.board = [['P', 'P', 'P', 'P', 'P'],
                   [' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' '],
                   ['N', 'N', 'N', 'N', 'N']]
    assert board.move_piece(0, 1, 'down-right', 'P') == True
    assert board.board[3][4] == 'P'


def test_move_piece_down_left(board):
    board.board = [['P', 'P', 'P', 'P', 'P'],
                   [' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' '],
                   ['N', 'N', 'N', 'N', 'N']]
    assert board.move_piece(0, 2, 'down-left', 'P') == True
    assert board.board[2][0] == 'P'
# neutron tests


def test_move_neutron_invalid_direction(board, monkeypatch):
    def mock_input(prompt):
        return 'invalid'
    monkeypatch.setattr('builtins.input', mock_input)

    assert board.move_neutron('invalid', 'O') == False


def test_move_neutron_move_to_the_wall(board, monkeypatch):
    board.board = [['P', 'P', 'P', 'P', 'P'],
                   [' ', ' ', ' ', ' ', ' '],
                   ['O', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' '],
                   ['N', 'N', 'N', 'N', 'N']]

    def mock_input(prompt):
        return 'left'
    monkeypatch.setattr('builtins.input', mock_input)

    assert board.move_neutron('left', 'O') == False


def test_move_neutron_move_next_to_the_piece(board, monkeypatch):
    board.board = [['P', 'P', 'P', ' ', 'P'],
                   [' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', 'O', 'P', ' '],
                   [' ', ' ', ' ', ' ', ' '],
                   ['N', 'N', 'N', 'N', 'N']]

    def mock_input(prompt):
        return 'right'
    monkeypatch.setattr('builtins.input', mock_input)

    assert board.move_neutron('right', 'O') == False


def test_move_neutron_valid(board, monkeypatch):
    def mock_input(prompt):
        return 'right'
    monkeypatch.setattr('builtins.input', mock_input)

    assert board.move_neutron('right', 'O') == True


def test_neutron_piece_up(board):
    assert board.move_neutron('up', 'O') == True
    assert board.board[1][2] == 'O'


def test_neutron_piece_down(board):
    board.board = [['P', 'P', 'P', 'P', 'P'],
                   ['O', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', 'N'],
                   [' ', ' ', ' ', ' ', ' '],
                   ['N', 'N', 'N', 'N', ' ']]
    assert board.move_neutron('down', 'O') == True
    assert board.board[3][0] == 'O'


def test_neutron_piece_left(board):
    board.board = [['P', 'P', 'P', 'P', 'P'],
                   [' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', 'O'],
                   [' ', ' ', ' ', ' ', ' '],
                   ['N', 'N', 'N', 'N', 'N']]
    assert board.move_neutron('left', 'O') == True
    assert board.board[2][0] == 'O'


def test_neutron_piece_right(board):
    board.board = [['P', 'P', 'P', ' ', ' '],
                   ['O', ' ', ' ', ' ', ' '],
                   ['N', ' ', ' ', 'P', 'P'],
                   [' ', ' ', ' ', ' ', ' '],
                   [' ', 'N', 'N', 'N', 'N']]
    assert board.move_neutron('right', 'O') == True
    assert board.board[1][4] == 'O'


def test_neutron_piece_up_right(board):
    board.board = [['P', 'P', 'P', 'P', 'P'],
                   [' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' '],
                   [' ', 'O', ' ', ' ', ' '],
                   ['N', 'N', 'N', 'N', 'N']]
    assert board.move_neutron('up-right', 'O') == True
    assert board.board[1][3] == 'O'


def test_neutron_piece_up_left(board):
    board.board = [['P', 'P', 'P', 'P', 'P'],
                   [' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', 'O', ' ', ' '],
                   ['N', 'N', 'N', 'N', 'N']]
    assert board.move_neutron('up-left', 'O') == True
    assert board.board[1][0] == 'O'


def test_move_neutron_down_right(board):
    board.board = [['P', 'P', 'P', 'P', 'P'],
                   [' ', 'O', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' '],
                   ['N', 'N', 'N', 'N', 'N']]
    assert board.move_neutron('down-right', 'O') == True
    assert board.board[3][3] == 'O'


def test_move_neutron_down_left(board):
    board.board = [['P', 'P', 'P', 'P', 'P'],
                   [' ', ' ', 'O', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' '],
                   ['N', 'N', 'N', 'N', 'N']]
    assert board.move_neutron('down-left', 'O') == True
    assert board.board[3][0] == 'O'


def test_check_winner_player1_on_first_condition(board):
    board.board = [['P', 'P', ' ', 'P', 'P'],
                   [' ', ' ', 'O', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' '],
                   ['N', 'N', 'N', 'N', 'N']]
    board.move_neutron('up', 'O')
    assert board.check_winner() == 'N'


def test_check_winner_player1_on_second_condition(board):
    board.board = [['P', 'P', 'O', 'P', 'P'],
                   [' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' '],
                   ['N', 'N', 'N', 'N', 'N']]
    board.move_piece(4, 2, 'left', 'N')
    assert board.check_winner() == 'N'


def test_check_winner_computer_on_first_condition(board):
    board.board = [['P', 'P', ' ', 'P', 'P'],
                   ['N', 'O', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' '],
                   ['N', ' ', 'N', 'N', 'N']]
    board.move_neutron('down', 'O')
    assert board.check_winner() == 'P'


def test_check_winner_computer_on_second_condition(board):
    board.board = [[' ', ' ', ' ', ' ', 'P'],
                   [' ', 'P', ' ', ' ', ' '],
                   ['P', 'O', ' ', 'P', ' '],
                   ['N', 'N', 'N', ' ', ' '],
                   [' ', ' ', ' ', 'N', 'N']]
    board.move_piece(2, 3, 'left', 'P')
    assert board.check_winner() == 'P'
