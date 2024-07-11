# Tic Tac Toe Game 
This project is a Python-based command-line game allows you to enjoy the classic Tic Tac Toe experience against an AI opponent.

## Table of Contents
- [Overview](#overview)
- [SetUp](#setup)
- [Functions](#functions)
- [Algorithm](#algorithm)
- [Contributing](#contributing)

<br>
    
## Overview
Tic Tac Toe is a beloved game that has entertained people of all ages for generations. This project aims to bring that timeless enjoyment to your command line interface. Whether you're looking to challenge a friend or hone your strategic skills against a computer opponent, this game provides an interactive and engaging experience.

- ## Features
  - Winning Logic: The game checks after each move for winning conditions and declares a winner or a draw when the game ends.
  - User-friendly Interface: Enjoy a clear and intuitive command-line interface that guides you through each game session.
    <br>
    <br>

## SetUp
- Install Dependencies:
  - Ensure Python 3.x is installed on your system.
  - Pygame

## Functions
- The player function takes a board state as input, and return which player’s turn it is (either X or O).
- The actions function returns a set of all of the possible actions that can be taken on a given board. Each action is represented by a tuple.
- The result function takes a board and an action as input, and should return a new board state, without modifying the original board. A deep copy of the board was made to use and modify.
- The winner function accepts a board as input, and return the winner of the board if there is one. Winners are either X or O and a tie returns None as the result.
- The terminal function accepts a board as input, and return a boolean value indicating whether the game is over.
- The utility function accepts a terminal board as input and output the utility of the board.
- The minimax function takes a board as input, and return the optimal move for the player to move on that board.

## Algorithm
The AI opponent uses the minimax algorithm to make strategic decisions:

- Maximize Win: The AI seeks to maximize its chances of winning by choosing moves that lead to victory.
- Minimize Loss: It also works to minimize the opponent's chances of winning, ensuring a challenging gameplay experience.

## Contributing
Contributions are welcome! If you have suggestions for improvements, bug fixes, or additional features, please open an issue to discuss your ideas.
