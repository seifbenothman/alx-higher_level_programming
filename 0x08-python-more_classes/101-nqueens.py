#!/usr/bin/python3
"""nqueens"""

from sys import argv

if __name__ == "__main__":
    chessboard = []
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if not argv[1].isdigit():
        print("N must be a number")
        exit(1)
    n = int(argv[1])
    if n < 4:
        print("N must be at least 4")
        exit(1)

    for i in range(n):
        chessboard.append([i, None])

    def is_queen_in_column(y):
        """Check"""
        for x in range(n):
            if y == chessboard[x][1]:
                return True
        return False

    def is_safe(x, y):
        """safe"""
        if is_queen_in_column(y):
            return False
        i = 0
        while i < x:
            if abs(chessboard[i][1] - y) == abs(i - x):
                return False
            i += 1
        return True

    def clear_chessboard(x):
        """Clears"""
        for i in range(x, n):
            chessboard[i][1] = None

    def solve_nqueens(x):
        """find"""
        for y in range(n):
            clear_chessboard(x)
            if is_safe(x, y):
                chessboard[x][1] = y
                if x == n - 1:
                    print(chessboard)
                else:
                    solve_nqueens(x + 1)

    solve_nqueens(0)
