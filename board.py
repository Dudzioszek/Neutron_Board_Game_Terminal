# import random

class NeutronBoard:
    def __init__(self):
        # Initialize the board with the starting positions of the pieces
        self.board = [['P', 'P', 'P', 'P', 'P'],
                      [' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', 'O', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' '],
                      ['N', 'N', 'N', 'N', 'N']]
        # # Initialize the current player
        # self.current_player = 'P'
        # Define the valid directions for the neutron to move
        self.directions = {
            'up': (-1, 0),
            'down': (1, 0),
            'left': (0, -1),
            'right': (0, 1),
            'up-right': (-1, 1),
            'up-left': (-1, -1),
            'down-right': (1, 1),
            'down-left': (1, -1)
        }

    def display_board(self):
        # Display the board
        print('\n\n')
        print('  | 0 | 1 | 2 | 3 | 4 |')
        print('-----------------------')
        for i, row in enumerate(self.board):
            print(f'{i} | {" | ".join(row)} |')
            print('-----------------------')

    def find_neutron(self):
        # Find the position of the neutron
        for i, row in enumerate(self.board):
            for j, piece in enumerate(row):
                if piece == 'O':
                    return i, j

    def move_piece(self, row, col, direction, color):

        try:
            row_offset, col_offset = self.directions[direction]
        except KeyError:
            print("You entered the wrong direction, please try again!")
            return False

        if self.board[row][col] != color:
            if color == 'O':
                print("Wrong Piece Error: You can't move neutron in this turn")
                return False
            print("Wrong Piece Error. You can't move other pieces")
            return False

        new_row = row + row_offset
        new_col = col + col_offset
        if new_row < 0 or new_row > 4 or new_col < 0 or new_col > 4:
            if color == 'N':
                print("Direction Error: You can't move to the wall that is next to you")
                return False
            return False
        if self.board[new_row][new_col] != ' ':
            if color == 'N':
                print("Direction Error: You can't move to the piece that is next to you")
                return False
            return False
        while new_row >= 0 and new_row <= 4 and new_col >= 0 and new_col <= 4 and self.board[new_row][new_col] == ' ':  # noqa: E501
            self.board[row][col] = ' '
            self.board[new_row][new_col] = color
            row = new_row
            col = new_col
            new_row += row_offset
            new_col += col_offset
        return True

    def check_winner(self):
        i, j = self.find_neutron()
        # Check if the neutron is blocked by the top or bottom wall
        if i == 0 or i == 4:
            return 'P' if i == 4 else 'N'
        # Check if the neutron is blocked by a piece or wall on all sides
        if (self.board[i-1][j] != ' ' and self.board[i+1][j] != ' ' and
                self.board[i][j-1] != ' ' and self.board[i][j+1] != ' '):
            # Check if the neutron is completely surrounded by pieces
            if (self.board[i-1][j] != 'N' and self.board[i+1][j] != 'N' and
                    self.board[i][j-1] != 'N' and self.board[i][j+1] != 'N'):
                return 'T'  # tie
            return 'P' if self.board[i-1][j] == 'N' or self.board[i+1][j] == 'N' or self.board[i][j-1] == 'N' or self.board[i][j+1] == 'N' else 'N'


        

    def move_neutron(self, direction, color):
        try:
            row_offset, col_offset = self.directions[direction]
        except KeyError:
            print("You entered the wrong direction, please try again!")
            return False
        row, col = self.find_neutron()
        new_row = row + row_offset
        new_col = col + col_offset
        if new_row < 0 or new_row > 4 or new_col < 0 or new_col > 4:
            if color == 'N':
                print("Direction Error: You can't move to the wall that is next to you")
                return False

            return False
        if self.board[new_row][new_col] != ' ':
            if color == 'N':
                print("Direction Error: You can't move to the piece that is next to you")
                return False
            return False

        while new_row >= 0 and new_row <= 4 and new_col >= 0 and new_col <= 4 and self.board[new_row][new_col] == ' ':  # noqa: E501
            self.board[row][col] = ' '
            self.board[new_row][new_col] = 'O'
            row = new_row
            col = new_col
            new_row += row_offset
            new_col += col_offset
        return True


