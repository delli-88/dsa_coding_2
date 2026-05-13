from collections import deque
class Solution:
    def pacificAtlantic(self, heights):
        
        n = len(heights)
        m = len(heights[0])

        pacific = [[False] * m for _ in range(n)]
        atlantic = [[False] * m for _ in range(n)]

        self.bfs(heights, pacific, [(r, 0) for r in range(n)] + [(0, c) for c in range(m)])
        self.bfs(heights, atlantic, [(r, m-1) for r in range(n)] + [(n-1, c) for c in range(m)])

        res = []
        for r in range(n):
            for c in range(m):
                if pacific[r][c] and atlantic[r][c]:
                    res.append([r, c])

        return res

    def bfs(self, heights, ocean, starts):
        n = len(heights)
        m = len(heights[0])

        queue = deque(starts)

        for r, c in starts:
            ocean[r][c] = True

        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (0 <= nr < n and 0 <= nc < m and
                    not ocean[nr][nc] and
                    heights[nr][nc] >= heights[r][c]):

                    ocean[nr][nc] = True
                    queue.append((nr, nc))
    
print(Solution().pacificAtlantic([[5,5,5,5],[4,4,4,4],[5,5,5,5]]))