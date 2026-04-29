from collections import deque
class Solution:
    def numIslands(self, grid) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = [[False for _ in range(m)] for _ in range(n)]
        islands = 0

        for r in range(n):
            for c in range(m):
                if grid[r][c] == "1" and not visited[r][c]:
                    islands += 1
                    self.traverseIsland(grid, visited, r, c)

        return islands

    def traverseIsland(self, grid, visited, row, col):
        n = len(grid)
        m = len(grid[0])
        queue = deque()
        
        queue.append((row, col))
        visited[row][col] = True

        while queue:
            r, c = queue.popleft()

            # top
            if r-1 >= 0 and grid[r-1][c] == "1" and not visited[r-1][c]:
                visited[r-1][c] = True
                queue.append((r-1, c))

            # bottom
            if r+1 < n and grid[r+1][c] == "1" and not visited[r+1][c]:
                visited[r+1][c] = True
                queue.append((r+1, c))
            
            # left
            if c-1 >= 0 and grid[r][c-1] == "1" and not visited[r][c-1]:
                visited[r][c-1] = True
                queue.append((r, c-1))
            
            # right
            if c+1 < m and grid[r][c+1] == "1" and not visited[r][c+1]:
                visited[r][c+1] = True
                queue.append((r, c+1))

sol = Solution()
print(sol.numIslands(grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))