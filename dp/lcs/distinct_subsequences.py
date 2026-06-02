class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        if len(t) > len(s):
            return 0
        
        dp = [[-1 for _ in range(len(t)+1)] for _ in range(len(s)+1)]
        return self.helper(s, t, 0, 0, dp)

    def helper(self, s: str, t: str, pos1, pos2, dp):

        if pos2 == len(t):
            dp[pos1][pos2] = 1
            return dp[pos1][pos2]
        
        if pos1 == len(s):
            dp[pos1][pos2] = 0
            return dp[pos1][pos2]
        
        if dp[pos1][pos2] !=-1:
            return dp[pos1][pos2]
        
        if s[pos1]!=t[pos2]:
            dp[pos1][pos2] = self.helper(s, t, pos1+1, pos2, dp)
            return dp[pos1][pos2]
        else:
            pick = self.helper(s, t, pos1+1, pos2+1, dp)
            skip = self.helper(s, t, pos1+1, pos2, dp)
            dp[pos1][pos2] = pick + skip
        return dp[pos1][pos2]

    def numDistinctTabulization(self, s: str, t: str) -> int:

        if len(t) > len(s):
            return 0
        
        dp = [[0 for _ in range(len(t)+1)] for _ in range(len(s)+1)]

        for i in range(len(s)+1):
            dp[i][-1] = 1

        for pos1 in range(len(s)-1, -1, -1):
            for pos2 in range(len(t)-1, -1, -1):
                if s[pos1]!=t[pos2]:
                    dp[pos1][pos2] = dp[pos1+1][pos2]
                else:
                    pick = dp[pos1+1][pos2+1]
                    skip = dp[pos1+1][pos2]
                    dp[pos1][pos2] = pick + skip

        return dp[0][0]

    def numDistinctTabulizationOptimization(self, s: str, t: str) -> int:

        if len(t) > len(s):
            return 0
        
        dp = [0 for _ in range(len(t)+1)]
        dp[-1] = 1

        for pos1 in range(len(s)-1, -1, -1):
            dpCopy = [0 for _ in range(len(t)+1)]
            dpCopy[-1] = 1
            for pos2 in range(len(t)-1, -1, -1):
                if s[pos1]!=t[pos2]:
                    dpCopy[pos2] = dp[pos2]
                else:
                    pick = dp[pos2+1]
                    skip = dp[pos2]
                    dpCopy[pos2] = pick + skip
            dp = dpCopy[:]

        return dp[0]


print(Solution().numDistinct(s = "babgbag", t = "bag"))
print(Solution().numDistinctTabulization(s = "babgbag", t = "bag"))
print(Solution().numDistinctTabulizationOptimization(s = "babgbag", t = "bag"))
print(Solution().numDistinctTabulizationOptimization(s = "rabbbit", t = "rabbit"))