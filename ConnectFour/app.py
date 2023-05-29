import numpy as np

# create the game board as a numpy array with 6 rows and 7 columns, filled with zeros
board = np.zeros((6,7))

# create a function to print the board
def print_board(board):
    print(np.flip(board, 0))

# create a function to check if a move is valid
def is_valid_move(board, col):
    return board[5][col] == 0

# create a function to drop a disc in the board
def drop_disc(board, row, col, disc):
    board[row][col] = disc

# create a function to get the next available row in a column
def get_next_row(board, col):
    for row in range(6):
        if board[row][col] == 0:
            return row

# create a function to check if a player has won
def is_winner(board, disc):
    # check horizontal
    for row in range(6):
        for col in range(4):
            if board[row][col] == disc and board[row][col+1] == disc and board[row][col+2] == disc and board[row][col+3] == disc:
                return True
    # check vertical
    for row in range(3):
        for col in range(7):
            if board[row][col] == disc and board[row+1][col] == disc and board[row+2][col] == disc and board[row+3][col] == disc:
                return True
    # check diagonal (down right)
    for row in range(3):
        for col in range(4):
            if board[row][col] == disc and board[row+1][col+1] == disc and board[row+2][col+2] == disc and board[row+3][col+3] == disc:
                return True
    # check diagonal (down left)
    for row in range(3):
        for col in range(3, 7):
            if board[row][col] == disc and board[row+1][col-1] == disc and board[row+2][col-2] == disc and board[row+3][col-3] == disc:
                return True

# create a function to play the game
def play_game():
    # set the initial player as player 1
    player = 1
    # loop until someone wins or the board is full
    while True:
        # print the board
        print_board(board)
        # ask the current player for a column to drop the disc
        col = int(input("Player " + str(player) + ", choose a column (0-6): "))
        # check if the move is valid
        if is_valid_move(board, col):
            # get the next available row in the column
            row = get_next_row(board, col)
            # drop the disc in the board
            drop_disc(board, row, col, player)
            # check if the player has won
            if is_winner(board, player):
                # print the board and the winner
                print_board(board)
                print("Congratulations Player " + str(player) + ", you won!")
                break
            # check if the board is full
            if np.count_nonzero(board == 0) == 0:
                # print the board and a tie message
                print_board(board)
                print("The game ended in a tie.")
                break
            # switch to the other player
            player = 2 if player == 1 else 1

play_game()