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
