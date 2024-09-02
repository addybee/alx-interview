#!/usr/bin/python3
"""
Nqueen algorithm
"""

import sys


def is_valid_position(board, row, col):
    """Check if the position (row, col) is safe for placing a queen.

    Args:
        board (list[list[int]]): The current state of the board.
        row (int): The row index where the queen is to be placed.
        col (int): The column index where the queen is to be placed.

    Returns:
        bool: True if the position is safe, False otherwise.
    """
    b_size = len(board)

    # Check the row and column for any other queen.
    if sum(board[row]) != 0 or any(board[i][col] for i in range(b_size)):
        return False

    # Check both diagonals for any other queen.
    for i, j in [(1, 1), (-1, -1), (1, -1), (-1, 1)]:
        r, c = row, col
        while 0 <= r + i < b_size and 0 <= c + j < b_size:
            r += i
            c += j
            if board[r][c]:
                return False
    return True


def place_next_queen(board, row):
    """Try to place a queen on the next valid position in the given row.

    Args:
        board (list[list[int]]): The current state of the board.
        row (int): The row index where the queen is to be placed.

    Returns:
        bool: True if a queen is successfully placed, False otherwise.
    """
    n = len(board)

    # Clear the row if a queen was already placed and start
    # searching from the next column.
    if 1 in board[row]:
        start_col = board[row].index(1) + 1
        board[row] = [0] * n
    else:
        start_col = 0

    # Try placing the queen in the next valid column.
    for col in range(start_col, n):
        if is_valid_position(board, row, col):
            board[row][col] = 1
            return True
    return False


def solve_nqueens(board, row=0, solutions=None):
    """Solve the N-Queens problem and collect all possible solutions.

    Args:
        board (list[list[int]]): The current state of the board.
        row (int): The current row being processed.
        solutions (list[list[list[int]]]): A list to collect all the solutions.

    Returns:
        None
    """
    if solutions is None:
        solutions = []

    n = len(board)

    while row < n:
        if place_next_queen(board, row):
            row += 1
        else:
            row -= 1
            if row < 0:
                return

        # If a solution is found, add it to the solutions list.
        if row == n:
            solutions.append([[r, board[r].index(1)] for r in range(n)])
            row -= 1

    if row == 0:
        return

    # Backtrack to find other possible solutions.
    solutions.append([[r, board[r].index(1)] for r in range(n)])
    idx = board[0].index(1)
    if idx > -1:
        board = [[0 for _ in range(n)] for _ in range(n)]
        board[0][idx] = 1
        solve_nqueens(board, 1, solutions)


def all_solution(n):
    """Run the N-Queens solver and print all solutions.

    Args:
        n (int): The size of the board (n x n).

    Returns:
        None
    """
    board = [[0] * n for _ in range(n)]
    solutions = []
    solve_nqueens(board, 0, solutions)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    input = sys.argv
    if len(input) != 2:
        print('Usage: nqueens N')
        exit(1)
    try:
        N = int(input[1])
        if N < 4:
            print('N must be at least 4')
        all_solution(N)
    except ValueError:
        print('N must be a number')
        exit(1)
