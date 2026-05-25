class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1 for _  in range(n)]
        return self.helper(0, n, dp)
    
    def helper(self, pos, n, dp):
        if pos > n:
            return 0
        
        if pos == n:
            return 1
        
        if dp[pos] > 0:
            return dp[pos]

        one = self.helper(1+pos, n, dp)
        two = self.helper(2+pos, n, dp)

        dp[pos] = one + two

        return dp[pos]

    def climbStairsTab(self, n: int) -> int:
        dp = [-1 for _  in range(n+1)]
        
        dp[n] = 1

        for i in range(n-1, -1, -1):
            one = dp[i+1]
            two = 0
            if i+2 <= n:
                two = dp[i+2]
            
            dp[i] = one + two
        
        print(dp)
        
        return dp[0]

    def climbStairsTabOpt(self, n: int) -> int:
        prev2 = 0
        prev1 = 1

        for _ in range(n-1, -1, -1):
            
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr
        
        return prev1
    
print(Solution().climbStairs(4))
print(Solution().climbStairsTab(4))