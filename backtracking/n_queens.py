class Solution:

    def solveNQueens(self, n):
        board = [["." for _ in range(n)] for _ in range(n)]
        sol = []
        self.helper(board, 0, sol)
        return sol

    def helper(self, board, row, sol):
        n = len(board)
        if row == n:
            temp = []
            for r in board:
                temp.append("".join(r))

            sol.append(temp)
            return

        for col in range(n):
            if self.canPlace(board, row, col):
                board[row][col] = "Q"
                self.helper(board, row + 1, sol)
                board[row][col] = "."

    def canPlace(self, board, row, col):

        n = len(board)

        # upper column
        r = row - 1
        while r >= 0:
            if board[r][col] == "Q":
                return False
            r -= 1

        # upper left diagonal
        r = row - 1
        c = col - 1

        while r >= 0 and c >= 0:
            if board[r][c] == "Q":
                return False
            r -= 1
            c -= 1

        # upper right diagonal
        r = row - 1
        c = col + 1
        while r >= 0 and c < n:
            if board[r][c] == "Q":
                return False
            r -= 1
            c += 1

        return True

print(Solution().solveNQueens(4))