def print_board(board):
    for row in board:
        print(" ".join(str(x) for x in row))
    print()

def is_safe(board,row,col,n):
    for i in range(row):
        if board[i][col]==1 or \
           (col-row+i >=0 and board[i][col-row+i]==1) or \
           (col+row-i <n and board[i][col+row-i]==1):
            return False
    return True

def solve(board,row,n):
    if(row==n):
        print_board(board)
        return
    for col in range(n):
        if is_safe(board,row,col,n):
            board[row][col]=1
            solve(board,row+1,n)
            board[row][col]=0

def nqueens():
    n=int(input("enter number"))
    board=[[0]*n for _ in range (n)]
    solve(board,0,n)

nqueens()