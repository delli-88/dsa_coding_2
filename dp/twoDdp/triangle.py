class Solution:
    def minimumTotal(self, triangle):
        dp = [[None for _ in range(len(triangle[i]))] for i in range(len(triangle))]
        print(dp)
        return self.helper(triangle, 0, 0, dp)
    
    def helper(self, triangle, pos1, pos2, dp):
        
        if pos1 == len(triangle)-1:
            dp[pos1][pos2] = triangle[pos1][pos2]
            return dp[pos1][pos2] 
        
        if dp[pos1][pos2]!=None:
            return dp[pos1][pos2]
        
        left = self.helper(triangle, pos1+1, pos2, dp)
        right = self.helper(triangle, pos1+1, pos2+1, dp)

        dp[pos1][pos2] = triangle[pos1][pos2] + min(left, right)

        return dp[pos1][pos2] 
    
    def minimumTotalTabulization(self, triangle):
        dp = [[None for _ in range(len(triangle[i]))] for i in range(len(triangle))]
    
        for pos1 in range(len(triangle)-1, -1, -1):
            for pos2 in range(len(triangle[pos1])-1, -1, -1):

                if pos1 == len(triangle)-1:
                    dp[pos1][pos2] = triangle[pos1][pos2]
                    continue
                
                left = dp[pos1+1][pos2]
                right = dp[pos1+1][pos2+1]

                dp[pos1][pos2] = triangle[pos1][pos2] + min(left, right)

        return dp[0][0] 

    def minimumTotalTabulizationOptimization(self, triangle):
        dp = [None for _ in range(len(triangle))]
        for pos1 in range(len(triangle)-1, -1, -1):
            dpCopy = dp.copy()
            for pos2 in range(len(triangle[pos1])-1, -1, -1):

                if pos1 == len(triangle)-1:
                    dpCopy[pos2] = triangle[pos1][pos2]
                    continue
                
                left = dp[pos2]
                right = dp[pos2+1]

                dpCopy[pos2] = triangle[pos1][pos2] + min(left, right)
            dp = dpCopy[:]

        return dp[0]

print(Solution().minimumTotal(triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]))
print(Solution().minimumTotalTabulization(triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]))
print(Solution().minimumTotalTabulizationOptimization(triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]))