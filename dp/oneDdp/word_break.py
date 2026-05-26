class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        dp = [-1 for _ in range(len(s)+1)]
        return self.helper(s, wordDict, 0, dp)

    def helper(self, s, wordDict, pos, dp):
        if pos == len(s):
            return True
        
        if dp[pos]!=-1:
            return dp[pos]
        
        for end in range(pos, len(s)):
        
            if s[pos:end+1] not in wordDict:
                continue

            if self.helper(s, wordDict, end+1, dp):
                return True

        dp[pos] = False 
        return dp[pos]

    def wordBreakTabulization(self, s: str, wordDict):

        dp = [False for _ in range(len(s)+1)]
        dp[-1] = True
        
        for pos in range(len(s)-1, -1, -1):
            for end in range(pos, len(s)):
            
                if s[pos:end+1] not in wordDict:
                    continue

                if dp[end+1]:
                    dp[pos] = True

        return dp[0]
    
print(Solution().wordBreak(s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]))