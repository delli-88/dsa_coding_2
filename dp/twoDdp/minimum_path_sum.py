class Solution:
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        dp =[[-1 for _ in range(n+1)] for _ in range(m+1)]
        return self.helper(grid, m, n, 0, 0, dp)
    
    def helper(self, grid, m, n, pos1, pos2, dp):

        if pos1 == m or pos2 == n:
            dp[pos1][pos2] = float("inf")
            return dp[pos1][pos2]
        
        if pos1 == m-1 and pos2 == n-1:
            dp[pos1][pos2] = grid[pos1][pos2]
            return dp[pos1][pos2]
        
        if dp[pos1][pos2]!=-1:
            return dp[pos1][pos2]

        right = self.helper(grid, m, n, pos1, pos2+1, dp)
        down = self.helper(grid, m, n, pos1+1, pos2, dp)
        dp[pos1][pos2] = grid[pos1][pos2] + min(right, down)

        return dp[pos1][pos2]

    def minPathSumTabulization(self, grid):
        m = len(grid)
        n = len(grid[0])
        dp =[[float("inf") for _ in range(n+1)] for _ in range(m+1)]

        for pos1 in range(m-1, -1, -1):
            for pos2 in range(n-1, -1, -1):

                if pos1 == m-1 and pos2 == n-1:
                    dp[pos1][pos2] = grid[pos1][pos2]
                    continue

                right = dp[pos1][pos2+1]
                down = dp[pos1+1][pos2]

                dp[pos1][pos2] = grid[pos1][pos2] + min(right, down)
        
        return dp[0][0]

    def minPathSumTabulizationOptimization(self, grid):
        m = len(grid)
        n = len(grid[0])
        dp =[float("inf") for _ in range(n+1)]

        for pos1 in range(m-1, -1, -1):
            for pos2 in range(n-1, -1, -1):

                if pos1 == m-1 and pos2 == n-1:
                    dp[pos2] = grid[pos1][pos2]
                    continue

                right = dp[pos2+1]
                down = dp[pos2]

                dp[pos2] = grid[pos1][pos2] + min(right, down)
        
        return dp[0]

print(Solution().minPathSum(grid = [[1,3,1],[1,5,1],[4,2,1]]))
print(Solution().minPathSumTabulization(grid = [[1,3,1],[1,5,1],[4,2,1]]))
print(Solution().minPathSumTabulizationOptimization(grid = [[1,3,1],[1,5,1],[4,2,1]]))