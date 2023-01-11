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
