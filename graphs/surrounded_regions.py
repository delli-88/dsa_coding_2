class Solution:

    def solve(self, board):

        rows = len(board)
        cols = len(board[0])

        vis = [[False] * cols for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and not vis[r][c]:
                    cells = []
                    surrounded = self.dfs(board, vis, r, c, cells)
                    if surrounded:
                        for x, y in cells:
                            board[x][y] = "X"

    def dfs(self, board, vis, r, c, cells):

        rows = len(board)
        cols = len(board[0])

        vis[r][c] = True

        cells.append((r, c))

        # assume surrounded initially
        surrounded = True

        # if touching boundary
        if (r == 0 or r == rows - 1 or c == 0 or c == cols - 1):
            surrounded = False

        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        for dr, dc in directions:

            nr = r + dr
            nc = c + dc

            if (0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "O" and not vis[nr][nc]):
                childSurrounded = self.dfs(board, vis, nr, nc, cells)
                surrounded = surrounded and childSurrounded

        return surrounded

        
print(Solution().solve([["O","O","O"],["O","O","O"],["O","O","O"]]))