class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[-1 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]
        return self.helper(word1, word2, 0, 0, dp)
    
    def helper(self, word1:str, word2:str, pos1, pos2, dp):

        if pos1 == len(word1) and pos2 == len(word2):
            dp[pos1][pos2] = 0
            return 0

        if pos2 == len(word2):
            dp[pos1][pos2] = len(word1) - pos1
            return dp[pos1][pos2] 
        
        if pos1 == len(word1):
            dp[pos1][pos2] = len(word2) - pos2
            return dp[pos1][pos2] 
        
        if dp[pos1][pos2] !=-1:
            return dp[pos1][pos2]
        
        if word1[pos1] == word2[pos2]:
            dp[pos1][pos2] = self.helper(word1, word2, pos1+1, pos2+1, dp)
        else:
            call1 = self.helper(word1, word2, pos1, pos2+1, dp)
            call2 = self.helper(word1, word2, pos1+1, pos2+1, dp)
            call3 = self.helper(word1, word2, pos1+1, pos2, dp)
            dp[pos1][pos2] = 1 + min(call1, call2, call3)

        return dp[pos1][pos2]

    def minDistanceTabulization(self, word1: str, word2: str) -> int:
        dp = [[0 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]

        for i in range(len(word1)):
            dp[i][-1] = len(word1) - i

        for j in range(len(word2)):
            dp[-1][j] = len(word2) - j
        
        for pos1 in range(len(word1)-1, -1, -1):
            for pos2 in range(len(word2)-1, -1, -1):
                if word1[pos1] == word2[pos2]:
                    dp[pos1][pos2] = dp[pos1+1][pos2+1]
                else:
                    call1 = dp[pos1][pos2+1]
                    call2 = dp[pos1+1][pos2+1]
                    call3 = dp[pos1+1][pos2]
                    dp[pos1][pos2] = 1 + min(call1, call2, call3)

        return dp[0][0]

    def minDistanceTabulizationOptimization(self, word1: str, word2: str) -> int:
        dp = [0 for _ in range(len(word2)+1)]

        for j in range(len(word2)+1):
            dp[j] = len(word2) - j

        for pos1 in range(len(word1)-1, -1, -1):
            dpCopy = [0 for _ in range(len(word2)+1)]
            dpCopy[-1] = len(word1) - pos1
            for pos2 in range(len(word2)-1, -1, -1):
                if word1[pos1] == word2[pos2]:
                    dpCopy[pos2] = dp[pos2+1]
                else:
                    insert = dpCopy[pos2+1]
                    replace = dp[pos2+1]
                    delete = dp[pos2]
                    dpCopy[pos2] = 1 + min(insert, replace, delete)
            dp = dpCopy[:]

        return dp[0]

print(Solution().minDistance(word1 = "horse", word2 = "ros"))
print(Solution().minDistanceTabulization(word1 = "horse", word2 = "ros"))
print(Solution().minDistanceTabulizationOptimization(word1 = "horse", word2 = "ros"))