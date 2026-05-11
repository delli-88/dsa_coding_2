from collections import deque
class Solution:
    def updateMatrix(self, mat):
        rows, cols = len(mat), len(mat[0])
        queue = deque()
        sol = [[-1] * cols for _ in range(rows)]

        # all 0s become BFS sources
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append((r, c))
                    sol[r][c] = 0

        dirs = [(-1,0),(1,0),(0,-1),(0,1)]

        # multi-source BFS
        while queue:

            r, c = queue.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < rows and
                    0 <= nc < cols and
                    sol[nr][nc] == -1
                ):
                    sol[nr][nc] = sol[r][c] + 1
                    queue.append((nr, nc))

        return sol

print(Solution().updateMatrix(mat = [[0,0,0],[0,1,0],[1,1,1]]))