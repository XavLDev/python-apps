winner = None
player1 = input("What is player 1's name?")
player2 = input("What is player 2's name?")
turn = player1

printUnderline = lambda x : print(f'\033[4m{x}\033[0m')
board = [
    [' ' ,' ', ' '],
    [' ' ,' ', ' '],
    [' ' ,' ', ' '],
]

def showBoard(board):
    header = '  |  1  |  2  |  3  |'
    printUnderline(header)

    printUnderline(f'a |  {board[0][0]}  |  {board[0][0]}  |  {board[0][0]}  |')
    printUnderline(f'b |  {board[0][0]}  |  {board[0][0]}  |  {board[0][0]}  |')
    printUnderline(f'c |  {board[0][0]}  |  {board[0][0]}  |  {board[0][0]}  |')

def checkWinner(board):
    # Insert the right numbers to check if the board is correct and return the mark if it is!

    print(board)
    ######################################################
    # Check row
    # Row 1
    if board[0][0] == board[0][0] == board[0][0] != " ":
        return board[0][0]

    # Row 2
    if board[0][0] == board[0][0] == board[0][0] != " ":
        return board[0][0]

    # Row 3
    if board[0][0] == board[0][0] == board[0][0] != " ":
        return board[0][0]

    #######################################################
    # Check column
    # Column 1
    if board[0][0] == board[0][0] == board[0][0] != " ":
        return board[0][0]

    # Column 2
    if board[0][0] == board[0][0] == board[0][0] != " ":
        return board[0][0]

    # Column 3
    if board[0][0] == board[0][0] == board[0][0] != " ":
        return board[0][0]

    #######################################################
    # Check cross
    # Top left > Bottom right
    if board[0][0] == board[0][0] == board[0][0] != " ":
        return board[0][0]

    # Top right > Bottom left
    if board[0][0] == board[0][0] == board[0][0] != " ":
        return board[0][0]

    return None


def isFull(board):
    string = ''
    for row in board:
        for cell in row:
            string += cell

    string = string.replace(" ", "")
    
    # Check if length of the string WITHOUT spaces is equal to 9
    full = len(string) == 9

    return full

showBoard(board)

#Game loop
# While there is None and the board is not full
while ??? and not isFull(board):

    # Player 1 starts with X
    if turn == player1:
        mark = 'X'
    else: 
        mark = 'O'


    print(f'It is {turn} turn right now')
    position = input(f'Where would you like to place your "{mark}" ')
    
    while len(position)!=2 or position[0] not in ['1','2','3'] or position[1] not in ['a','b','c']:
        position = input(f'Please place your "{mark}" in a valid position')
    
    # Place mark
    board[['1','2','3'].index(position[0])][['a','b','c'].index(position[1])] = mark

    showBoard(board)

    # Change turn
    if turn == player1:
        turn = player2
    else:
        turn = player1

    # Check if board has a winner
    winner = checkWinner(board)


if winner is None:
    print(f'Draw! There is no winner')
else:
    winner = ''
    if turn != player1:
        winner = player1
    else:
        winner = player2
    
    print(f'The winner is \033[95m{winner}\033[0m!')
