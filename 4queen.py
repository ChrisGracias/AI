def is_safe(board, row, col):
    # Check if there is a queen in the same row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, 4, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_queens(board, col):
    if col >= 4:
        return True

    for i in range(4):
        if is_safe(board, i, col):
            board[i][col] = 1

            if solve_queens(board, col + 1):
                return True

            board[i][col] = 0

    return False

def print_solution(board):
    for i in range(4):
        for j in range(4):
            print(board[i][j], end=" ")
        print()

board = [[0 for _ in range(4)] for _ in range(4)]

if solve_queens(board, 0):
    print("Solution exists:")
    print_solution(board)
else:
    print("Solution does not exist.")
