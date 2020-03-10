import random
#--------------------All the functions needed-------------------------------------------------
def check_for_win():
    # rows
    for i in range(3):
        xCount_row = 0
        oCount_row = 0
        for j in range(3):
            if(board[i][j] == 'X'):
                xCount_row += 1
            if(board[i][j] == 'O'):
                oCount_row += 1
        if(xCount_row == 3):
            return 1
        if(oCount_row == 3):
            return 2
    # columns
    for i in range(3):
        xCount_col = 0
        oCount_col = 0
        for j in range(3):
            if(board[j][i] == 'X'):
                xCount_col += 1
            if(board[j][i] == 'O'):
                oCount_col += 1
        if(xCount_col == 3):
            return 1
        if(oCount_col == 3):
            return 2
    # main diagonal
    xCount_diag = 0
    oCount_diag = 0
    for i in range(3):
        if(board[i][i] == 'X'):
            xCount_diag += 1
        if(board[i][i] == 'O'):
            oCount_diag += 1
    if(xCount_diag == 3):
        return 1
    if(oCount_diag == 3):
        return 2
    # secondary diagonal
    xCount_diag2 = 0
    oCount_diag2 = 0
    for i in range(3):
        for j in range(3):
            if(i+j == 2):
                if(board[i][j] == 'X'):
                    xCount_diag2 += 1
                if(board[i][j] == 'O'):
                    oCount_diag2 += 1
    if(xCount_diag2 == 3):
        return 1
    if(oCount_diag2 == 3):
        return 2
    return 0
#--------------------------------------------------------------------------
def human_move():
    global board
    global legalMoves
    global moves
    global flag
    i = int(input("Enter i (1-3).."))
    i -= 1
    j = int(input("Enter j (1-3).."))
    j -= 1
    while(legalMoves[i][j] == 1):
        print("Illegal move, try again..")
        i = int(input("Enter i (1-3).."))
        i -= 1
        j = int(input("Enter j (1-3).."))
        j -= 1
    if(board[i][j] == None):
        if(flag):
            board[i][j] = 'X'
        else:
            board[i][j] = 'O'
        legalMoves[i][j] = 1
        moves += 1
#--------------------------------------------------------------------------
def computer_move():
    global board
    global legalMoves
    global flag
    global moves
    i = random.randrange(0, 3)
    j = random.randrange(0, 3)
    while(legalMoves[i][j] == 1):
        i = random.randrange(0, 3)
        j = random.randrange(0, 3)
    if(board[i][j] == None):
        if(not flag):
            board[i][j] = 'X'
        else:
            board[i][j] = 'O'
        moves += 1
        legalMoves[i][j] = 1
#--------------------------------------------------------------------------
def print_board():
    print("-------------------------------")
    for i in range(3):
        print(board[i])
    print("-------------------------------")
#--------------------------------------------------------------------------
def print_instructions():    
    print("TIC-TAC-TOE")
    print("game instructions are as follows:")
    print("when it's your turn, write the coordinates of where you want to place your move (i,j)")
    print("Note: whoever goes first gets X")
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
print_instructions()
first = str(input("pick who goes first (H/C):"))
win = 0  # values: 0 for tie, 1 for X, and 2 for O
flag = False
turn = 0
board = [[None] * 3 for i in range(3)]
legalMoves = [[0] * 3 for i in range(3)]
# turn = 0 for human, turn = 1 for computer
if(first == 'H'):
    flag = True
if(flag):  # Human goes first
    i = int(input("Enter i (1-3).."))
    i -= 1
    j = int(input("Enter j (1-3).."))
    j -= 1
    turn = 0
else:
    i = random.randrange(0, 3)
    j = random.randrange(0, 3)
    turn = 1
legalMoves[i][j] = 1
board[i][j] = 'X'
turn = (turn + 1) % 2
moves = 1  # max of 9 moves
while(win == 0 and moves <= 9):
    # print the board:
    print_board()
    if(turn == 0):  # human turn
        print("your turn...")
        human_move()
    else:  # computer turn
        print("computer turn...")
        computer_move()
    turn = (turn + 1) % 2  # next turn
    # check for win
    win = check_for_win()
# print the board:
print_board()
if(win == 0):
    print("it's a tie")
elif(win == 1):
    print("X wins")
else:
    print("O wins")
