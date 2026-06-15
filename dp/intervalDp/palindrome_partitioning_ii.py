class Solution:
    def minCut(self, s: str) -> int:
        dp = [-1 for _ in range(len(s)+1)]
        palindromesPreCompute = self.getPalindromePreCompute(s)
        return self.helper(s, 0, palindromesPreCompute, dp)
    
    def helper(self, s:str, pos, pc, dp):

        if pos == len(s):
            return 0
        
        if dp[pos] != -1:
            return dp[pos]
        
        mini = float("inf")
        for end in range(pos, len(s)):

            if not pc[pos][end]:
                continue
            mini = min(mini, self.helper(s, end+1, pc, dp))
        
        dp[pos] = 1 + mini
        return dp[pos]

    def getPalindromePreCompute(self, s):

        dp = [[True for _ in range(len(s)+1)] for _ in range(len(s)+1)]
        for start in range(len(s)-1, -1, -1):
            for end in range(start, len(s)):
                if s[start] != s[end]:
                    dp[start][end] = False
                else:
                    dp[start][end] = dp[start+1][end-1]
        return dp

print(Solution().minCut(s = "cabaddab"))