
# -1 if the board is not yet finished (there are empty spots),
# 1 if "X" won,
# 2 if "O" won,
# 0 if it's a cat's game (i.e. a draw).

def is_solved(board):
    
    # check for
    # Rows
    for row in board:
        if row[0] != 0 and row[0] == row[1] and row[1] == row[2]:
            answer = row[0]
            print( 'Row wins:' , answer )
            return answer

    # Columns
    for row in range( len( board ) ):
        if board[0][row] != 0 and board[0][row] == board[1][row] and board[1][row] == board[2][row]:
            answer = board[0][row]
            print( 'Column wins:' , answer )
            return answer

    # diagonal
    diagonals = [ [ board[0][0] , board[1][1] , board[2][2] ] , [ board[2][0] , board[1][1] , board[0][2] ] ]
    
    for i in diagonals:
        if i[0] != 0 and i[0] == i[1] and i[1] == i[2]:
            answer = i[0]
            print( 'Diagonal wins:' , answer )
            return answer

    # not finished
    for row in board:
        if 0 in row:
            answer = -1
            print( 'Incomplete:' , answer )
            return answer

    # draw
    answer = 0
    print( 'Draw:' , answer )        
    return answer



board = [[1, 1, 1],
         [0, 2, 2],
         [0, 0, 0]]
is_solved(board) # 1 winning row

board = [[2, 1, 2],
         [2, 1, 1],
         [1, 1, 2]]
is_solved(board) # 1 winning column

board = [[2, 2, 1],
         [2, 1, 1],
         [1, 1, 2]]
is_solved(board) # 1 winning diagonal

board = [[0, 0, 1],
         [0, 1, 2],
         [2, 1, 0]]
is_solved(board) # -1 not yet finished

board = [[2, 1, 2],
         [2, 1, 1],
         [1, 2, 1]]
is_solved(board) # 0 draw