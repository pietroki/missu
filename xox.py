# Import the necessary modules.
import random
import os

# Define the game board.
board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

# Define the players.
players = ['X', 'O']

# Get the player's names.
player1_name = input("Enter the name of player 1: ")
player2_name = input("Enter the name of player 2: ")

# Set the current player to player 1.
current_player = players[0]

# Define a function to print the game board.
def print_board():
    for row in board:
        for cell in row:
            print(cell, end=" ")
        print()

# Define a function to get the player's move.
def get_move(player):
    while True:
        try:
            row = int(input("Enter the row (1-3): ")) - 1
            column = int(input("Enter the column (1-3): ")) - 1
            if row < 0 or row > 2 or column < 0 or column > 2:
                raise ValueError
            if board[row][column] != ' ':
                raise ValueError
            return row, column
        except ValueError:
            print("Invalid move. Please try again.")

# Define a function to check if the game is over.
def check_game_over():
    # Check if there is a winner.
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return True
    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column] and board[0][column] != ' ':
            return True
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return True

    # Check if there is a tie.
    for row in board:
        for cell in row:
            if cell == ' ':
                return False

    return True

# Define a function to play the game.
def play_game():
    # Print the game board.
    print_board()

    # While the game is not over, get the player's move and update the game board.
    while not check_game_over():
        # Get the player's move.
        row, column = get_move(current_player)

        # Update the game board.
        board[row][column] = current_player

        # Print the game board.
        print_board()

        # Check if the game is over.
        if check_game_over():
            break

        # Switch the current player.
        current_player = players[(players.index(current_player) + 1) % 2]

    # Print the winner.
    if check_game_over():
        print(f"{current_player} wins!")
    else:
        print("Tie!")

# Play the game.
play_game()
