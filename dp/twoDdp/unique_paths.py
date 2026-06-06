class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp =[[-1 for _ in range(n+1)] for _ in range(m+1)]
        return self.helper(m, n, 0, 0, dp)
    
    def helper(self, m, n, pos1, pos2, dp):

        if pos1 == m or pos2 == n:
            dp[pos1][pos2] = 0
            return dp[pos1][pos2]
        
        if pos1 == m-1 and pos2 == n-1:
            dp[pos1][pos2] = 1
            return dp[pos1][pos2]
        
        if dp[pos1][pos2]!=-1:
            return dp[pos1][pos2]

        right = self.helper(m, n, pos1, pos2+1, dp)
        down = self.helper(m, n, pos1+1, pos2, dp)
        dp[pos1][pos2] = right+down

        return dp[pos1][pos2]

    def uniquePathsTabulization(self, m, n):
        dp =[[0 for _ in range(n+1)] for _ in range(m+1)]

        for pos1 in range(m-1, -1, -1):
            for pos2 in range(n-1, -1, -1):

                if pos1 == m-1 and pos2 == n-1:
                    dp[pos1][pos2] = 1
                    continue

                right = dp[pos1][pos2+1]
                down = dp[pos1+1][pos2]

                dp[pos1][pos2] = right + down
        
        return dp[0][0]

    def uniquePathsTabulizationOptimization(self, m, n):
        dp =[0 for _ in range(n+1)]

        for pos1 in range(m-1, -1, -1):
            for pos2 in range(n-1, -1, -1):

                if pos1 == m-1 and pos2 == n-1:
                    dp[pos2] = 1
                    continue

                right = dp[pos2+1]
                down = dp[pos2]

                dp[pos2] = right + down
        
        return dp[0]


    
print(Solution().uniquePaths(m = 3, n = 7))
print(Solution().uniquePathsTabulization(3,7))
print(Solution().uniquePathsTabulizationOptimization(3,7))