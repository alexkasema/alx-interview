#!/usr/bin/python3
""" The N queens puzzle """
import sys


def is_safe(board, row, col, N):
    """
    Checks if queen can be placed at board[row][col].
    """
    # check column on the left side
    for i in range(row):
        if board[i] == col:
            # There is already a queen in this column
            return False

    # check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i] == j:
            # There is already a queen in this upper diagonal
            return False

    # check lower diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i] == j:
            # There is already a queen in this lower diagonal
            return False

    # No conflicts, safe to place the queen
    return True


def solve_nqueens(N):
    """
    Solves the N Queens problem using backtracking
    """
    # Initialize the board, -1 indicates no queen is placed on that row
    board = [-1] * N
    # list to store all solutions
    result = []

    def backtrack(row):
        """
        Helper function to place queens row by row
        """

        if row == N:
            # All queens placed successfully, add the solution to the result
            result.append(board[:])
            return

        for col in range(N):
            if is_safe(board, row, col, N):
                # place queen at (row, col)
                board[row] = col
                # move to the next row
                backtrack(row + 1)
                # Remove the queen (backtrack)
                board[row] = -1
    # start placing queens from the first row
    backtrack(0)
    # Return all possible solutions
    return result


def print_solutions(solutions, N):
    """
    Prints the solutions in the required format.
    """
    for solution in solutions:
        formatted_solution = [[i, solution[i]] for i in range(N)]
        print(formatted_solution)


def main():
    """
    Handle command-line arguments and solve the problem.
    """

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)
    print_solutions(solutions, N)


if __name__ == '__main__':
    main()
