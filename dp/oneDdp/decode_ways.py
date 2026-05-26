class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [-1 for _ in range(len(s)+1)]
        return self.helper(s, 0, dp)
    
    def helper(self, s, pos, dp):

        if pos == len(s):
            return 1
        
        if not self.isValid(s[pos]):
            return 0
        
        if dp[pos]!=-1:
            return dp[pos]

        one = self.helper(s, pos+1, dp)
        two = 0
        if pos+1<len(s) and self.isValid(s[pos]+s[pos+1]):
            two = self.helper(s, pos+2, dp)
        
        dp[pos] = one + two
        
        return dp[pos]

    def numDecodingsTabulation(self, s):
        dp = [0 for _ in range(len(s)+1)]
        dp[-1] = 1
        
        for i in range(len(s)-1, -1, -1):
            
            if not self.isValid(s[i]):
                continue

            one = dp[i+1]
            two = 0
            if i+1 < len(s) and self.isValid(s[i]+s[i+1]):
                two = dp[i+2]
            
            dp[i] = one + two

        return dp[0]

    def numDecodingsTabulationOptimization(self, s):
        next1 = 1
        next2 = 1
        
        for i in range(len(s)-1, -1, -1):
            
            if not self.isValid(s[i]):
                next2 = next1
                next1 = 0
                continue

            one = next1
            two = 0
            if i+1 < len(s) and self.isValid(s[i]+s[i+1]):
                two = next2
            
            curr = one + two
            next2 = next1
            next1 = curr

        return next1


        
    def isValid(self, s):        
        if int(s) <=0 or int(s)>26:
            return False
        return True
 
print(Solution().numDecodings("10211"))
print(Solution().numDecodingsTabulation("10211"))
print(Solution().numDecodingsTabulationOptimization("10211"))