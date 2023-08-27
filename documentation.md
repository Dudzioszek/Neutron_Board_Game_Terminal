# Neutron Game Documentation

## Introduction

This document provides a detailed overview of the Neutron game implemented in Python. The game simulates a board game where players move pieces on a board with the objective of achieving a winning condition.

## Modules

### 1. board.py

#### `NeutronBoard` class:
- **Attributes**:
  - `board`: A 5x5 list representing the game board's state.
- **Methods**:
  - `__init__(self)`: Initializes the board with starting positions.
  - ... (other methods related to board manipulation and game state checks)

### 2. player.py

#### `Player` class:
- **Attributes**:
  - `board`: Reference to the game board.
  - `color`: Color of the player's pieces (e.g., 'N').
  - `strategy`: Strategy the player follows ('human', 'random', or 'smart').
- **Methods**:
  - `make_move(self)`: Depending on the strategy, it prompts the player to make a move or makes an automated move.

### 3. game.py

#### `Game` class:
- **Attributes**:
  - `board`: An instance of `NeutronBoard`.
  - `player1`: An instance of `Player`.
- **Methods**:
  - `__init__(self)`: Initializes the game board and players.
  - ... (other methods related to the game flow and turn mechanics)

### 4. main.py

Contains the main function to initialize and start the game.

### 5. test_board.py and test_player.py

These modules contain unit tests for the `NeutronBoard` and `Player` classes, respectively.

## Gameplay

The game starts with a 5x5 board where pieces are positioned in their starting locations. Players take turns moving their pieces with the objective of achieving a specific game condition (not detailed in the provided content).

For a computer player, two strategies are available: 'random' where moves are chosen at random, and 'smart' where moves are chosen based on some predefined logic.

## Conclusion

This documentation provides an understanding of the Neutron game's structure and functionalities. For a hands-on experience, it's recommended to run the `main.py` script and play the game. For developers, the unit tests provide a means to validate any changes or enhancements made to the game logic.
