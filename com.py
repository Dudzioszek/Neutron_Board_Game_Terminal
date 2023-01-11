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


    # def move_neutron(self, direction):
    #     # Check if the direction is valid
    #     try:
    #         direction_offset = self.directions[direction]
    #     except KeyError:
    #         return False  # Invalid direction
    #     # Find the current position of the neutron
    #     row, col = self.find_neutron()
    #     # Keep moving the neutron in the specified direction until it reaches the end of the board or a square that is not empty # noqa: E501
    #     while True:
    #         new_row = row + direction_offset[0]
    #         new_col = col + direction_offset[1]
    #         if not (0 <= new_row < 5 and 0 <= new_col < 5):
    #             # The neutron has reached the end of the board
    #             break
    #         if self.board[new_row][new_col] != ' ':
    #             # The neutron has reached a square that is not empty
    #             break
    #         # Update the position of the neutron
    #         self.board[row][col] = ' '
    #         self.board[new_row][new_col] = 'O'
    #         row, col = new_row, new_col
    #     return True
import random


class Player:
    def __init__(self, board, color, strategy):
        self.board = board
        self.color = color
        self.strategy = strategy

    def make_move(self):
        if self.strategy == 'human':
            # Prompt the player to enter a move
            while True:
                print('Player1:')
                move = input('Enter your move (row column direction): ')
                try:
                    row, col, direction = move.split()
                    row, col = int(row), int(col)
                    if self.board.move_piece(row, col, direction, self.color):
                        return True
                except ValueError:
                    print('Wrong input, try again!')
                    pass
        elif self.strategy == 'random':
            # Choose a random move
            while True:
                row = int(random.randint(0, 4))
                col = int(random.randint(0, 4))
                direction = random.choice([('up'), ('down'), ('left'), ('right'), ('up-right'), ('up-left'), ('down-right'), ('down-left')])  # noqa: E501
                if self.board.move_piece(row, col, direction, self.color):
                    return True
        elif self.strategy == 'smart':
            """

            1.define a list of all possible directions that a piece can be moved.

            2.Defines a function that calculates the distance 
            of a given piece to the nearest wall in each direction. 

            3.Sort the directions by the distance to the nearest wall, 
            with the shortest distance first. This allows you to prioritize 
            moving the piece in a direction that brings it closer to a wall.

            4.Finally, you could try to move the piece in each direction, 
            starting with the direction with the shortest distance to a wall, 
            until the move is successful. If no moves are successful, 
            you could return False to indicate that the move was not possible.
            """
        
            # Find the current position of the neutron
            neutron_row, neutron_col = self.board.find_neutron()

            # Find the coordinates of all the player's pieces
            piece_coords = []
            for i in range(5):
                for j in range(5):
                    if self.board.board[i][j] == self.color:
                        piece_coords.append((i, j))

            # Calculate the distance from each piece to the neutron
            distances = [(abs(row - neutron_row) + abs(col - neutron_col)) for row, col in piece_coords]

            # Find the index of the piece that is closest to the neutron
            min_index = distances.index(min(distances))

            # Calculate the distance from the chosen piece to the nearest wall in each direction
            row, col = piece_coords[min_index]
            distances = {
                'up': row,
                'down': 4 - row,
                'left': col,
                'right': 4 - col,
                'up-right': min(row, 4 - col),
                'up-left': min(row, col),
                'down-right': min(4 - row, 4 - col),
                'down-left': min(4 - row, col)
            }

            # Sort the directions by the distance to the nearest wall
            sorted_distances = sorted(distances.items(), key=lambda x: x[1])

            # Try to move the piece in the direction with the smallest distance
            # to a wall
            for direction, distance in sorted_distances:
                if self.board.move_piece(row, col, direction, self.color):
                    return True


    def make_neutron_move(self):
        if self.strategy == 'human':
            # Prompt the player to enter a move
            while True:
                direction = input('Enter the direction to move the neutron: right, left, down, up, down-right down-left, up-right and up-left: ')  # noqa: E501
                try:
                    if self.board.move_neutron(direction, self.color):
                        return True
                except ValueError:
                    print('Wrong input, try again!')
        elif self.strategy == 'random':
            while True:
                direction = random.choice([('up'), ('down'), ('left'), ('right'), ('up-right'), ('up-left'), ('down-right'), ('down-left')])  # noqa: E501
                if self.board.move_neutron(direction, self.color):
                    return True
        elif self.strategy == 'smart':
            """
            1. Determine the current position of the neutron on the board.
            2. Calculate the distance from each of your pieces to the neutron. 
            The piece that is closest to the neutron is the one that should be moved.
            3.Calculate the distance from the piece to the closest wall in each direction. 
            The direction with the smallest distance is the one that the piece should move towards.
            4.Move the piece in the chosen direction as far as possible.
            """
            # Find the current position of the neutron
            row, col = self.board.find_neutron()

            # Calculate the distance to the closest wall in each direction
            distances = {
                'up': row,
                'down': 4 - row,
                'left': col,
                'right': 4 - col,
                'up-right': min(row, 4 - col),
                'up-left': min(row, col),
                'down-right': min(4 - row, 4 - col),
                'down-left': min(4 - row, col)
            }

            # Sort the directions by the distance to the nearest wall
            sorted_distances = sorted(distances.items(), key=lambda x: x[1])

            # Try to move the neutron in the direction with the smallest distance
            # to a wall
            for direction, distance in sorted_distances:
                if self.board.move_neutron(direction, self.color):
                    break
from board import NeutronBoard
from player import Player


class Game:
    def __init__(self):
        self.board = NeutronBoard()
        self.player1 = Player(self.board, 'N', 'human')
        # Prompt the user to choose which strategy the computer should use
        while True:
            strategy = input(
                "Choose the strategy for the computer: random or smart: ")
            if strategy == 'random' or strategy == 'smart':
                break
            else:
                print("Input Error: Please input th ecorrect strategy of your opponent")
        self.player2 = Player(self.board, 'P', strategy)
        self.winner_names = {
            "P": "Player",
            "C": "Computer"
        }
        self.color = 'Blank variable'

    def play(self):
        # Starting move
        self.board.display_board()
        self.player1.make_neutron_move()
        while True:
            # Player 2's (computer) turn
            self.player2.make_neutron_move()
            if self.board.check_winner() is not None:
                break

            self.player2.make_move()
            if self.board.check_winner() is not None:
                if self.board.check_winner() == 'T':
                    self.board.check_winner() == str(self.player2.color)
                    break
                break

            # Player 1's turn
            self.board.display_board()
            self.player1.make_move()

            if self.board.check_winner() is not None:
                if self.board.check_winner() == 'T':
                    self.board.check_winner() == str(self.player1.color)
                    break
                break

            self.board.display_board()
            self.player1.make_neutron_move()

            if self.board.check_winner() is not None:
                break

        winner = self.board.check_winner()
        if winner == 'N':
            self.board.display_board()
            print('Player 1 wins!')
        elif winner == 'P':
            self.board.display_board()
            print('Player 2 (computer) wins!')
        else:
            pass
