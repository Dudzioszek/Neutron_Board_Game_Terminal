
# Neutron Game Implementation

## Overview

This project is a Python implementation of the Neutron game. The game consists of a board and player mechanics that allow for both human and computer opponents. The project is structured with separate modules for the board, game flow, players, and unit tests.

## Features

- **Game Board:** A 5x5 game board (`NeutronBoard`) initialized with starting positions for game pieces.
- **Player Mechanics:** Support for both human input and computer strategies (random or smart) for playing moves.
- **Game Flow:** An integrated game flow (`Game` class) that controls the sequence of play, player turns, and game termination conditions.
- **Unit Tests:** Tests for both the `NeutronBoard` and `Player` classes to ensure game logic correctness.

## How to Play

1. Run the `main.py` script to start the game.
2. For the computer opponent, choose the desired strategy (random or smart).
3. Follow on-screen instructions to make moves.

## Prerequisites

- Python 3.x
- pytest (for running unit tests)

## Installation & Running

1. Clone or download this repository.
2. Navigate to the directory containing the source files.
3. Start the game:

```bash
python main.py
```

4. To run unit tests:

```bash
pytest test_board.py
pytest test_player.py
```

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## License

This project is under the MIT License. See the LICENSE file for more details.

## Acknowledgments

- The game Neutron for the inspiration behind this implementation.
