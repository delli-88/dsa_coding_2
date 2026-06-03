class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        dp = [[-1 for _ in range(len(str2)+1)] for _ in range(len(str1)+1)]
        self.helper(str1, str2, 0, 0, dp)
        print(dp)
        
        i, j = 0,0
        res = []
        while i<len(str1) and j<len(str2):

            if str1[i] == str2[j]:
                res.append(str1[i])
                i += 1
                j += 1
            else:
                if dp[i][j+1] < dp[i+1][j]:
                    res.append(str2[j])
                    j += 1
                else:
                    res.append(str1[i])
                    i += 1

        if i == len(str1):
            res.append(str2[j:])
        
        if j == len(str2):
            res.append(str1[i:])

        return "".join(res)
    
    def helper(self, str1: str, str2: str, pos1, pos2, dp):

        if pos1 ==  len(str1):
            dp[pos1][pos2] = len(str2) - pos2
            return dp[pos1][pos2]
        
        if pos2 == len(str2):
            dp[pos1][pos2] = len(str1) - pos1
            return dp[pos1][pos2] 
        
        if dp[pos1][pos2] != -1:
            return dp[pos1][pos2]

        if str1[pos1] == str2[pos2]:
            dp[pos1][pos2] = 1 + self.helper(str1, str2, pos1+1, pos2+1, dp)
        else:
            dp[pos1][pos2] = 1 + min(
                self.helper(str1, str2, pos1+1, pos2, dp),
                self.helper(str1, str2, pos1, pos2+1, dp)
            )        
        return dp[pos1][pos2]

print(Solution().shortestCommonSupersequence(str1 = "abac", str2 = "cab"))
print(Solution().shortestCommonSupersequence(str1 = "sabcrat", str2 = "xbcrat"))