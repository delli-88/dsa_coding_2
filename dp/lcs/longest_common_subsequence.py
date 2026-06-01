class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        dp = [[-1 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]
        return self.helper(text1, text2, 0, 0, dp)
    
    def helper(self, text1, text2, pos1, pos2, dp):

        if pos1 == len(text1) or pos2 == len(text2):
            return 0
        
        if dp[pos1][pos2]!=-1:
            return dp[pos1][pos2]
        
        if text1[pos1] == text2[pos2]:
            dp[pos1][pos2] = 1 + self.helper(text1, text2, pos1+1, pos2+1, dp)
        else:
            dp[pos1][pos2] = max(
                self.helper(text1, text2, pos1+1, pos2, dp),
                self.helper(text1, text2, pos1, pos2+1, dp)
            )
        
        return dp[pos1][pos2]
    
    def longestCommonSubsequenceTabulization(self, text1, text2):
        dp = [[0 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]

        for pos1 in range(len(text1)-1, -1, -1):
            for pos2 in range(len(text2)-1, -1, -1):

                if pos1+1 > len(text1) and pos2+1 > len(text2):
                    continue

                if text1[pos1] == text2[pos2]:
                    dp[pos1][pos2] = 1 + dp[pos1+1][pos2+1]
                else:
                    dp[pos1][pos2] = max(dp[pos1+1][pos2], dp[pos1][pos2+1])

        return dp[0][0]

    def longestCommonSubsequenceTabulizationOptimization(self, text1, text2):
        dp = [0 for _ in range(len(text2)+1)]

        for pos1 in range(len(text1)-1, -1, -1):
            dpCopy = dp.copy()
            for pos2 in range(len(text2)-1, -1, -1):

                if pos1+1 > len(text1) and pos2+1 > len(text2):
                    continue

                if text1[pos1] == text2[pos2]:
                    dpCopy[pos2] = 1 + dp[pos2+1]
                else:
                    dpCopy[pos2] = max(dp[pos2], dpCopy[pos2+1])
            dp = dpCopy[:]
                    
        return dp[0]

print(Solution().longestCommonSubsequence(text1 = "abcde", text2 = "ace"))
print(Solution().longestCommonSubsequenceTabulization(text1 = "abcde", text2 = "ace"))
print(Solution().longestCommonSubsequenceTabulizationOptimization(text1 = "abcde", text2 = "ace"))