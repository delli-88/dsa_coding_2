class Solution:
    def change(self, amount: int, coins) -> int:
        dp = [[-1 for _ in range(amount+1)] for _ in range(len(coins))]
        res = self.helper(coins, amount, 0, 0, dp)
        return res

    def helper(self, coins, amount, total, pos, dp):

        if total > amount or pos >= len(coins):
            return 0
        
        if amount == total:
            dp[pos][total] = 1
            return dp[pos][total]

        if dp[pos][total] != -1:
            return dp[pos][total]
        
        pick = self.helper(coins, amount, total + coins[pos], pos, dp)
        no_pick = self.helper(coins, amount, total, pos+1, dp)
        
        dp[pos][total] = pick + no_pick

        return dp[pos][total]

    def coinChangeTabulization(self, coins, amount):
        n = len(coins)

        dp = [[0 for _ in range(amount + 1)] for _ in range(n + 1)]

        for pos in range(n + 1):
            dp[pos][amount] = 1

        for pos in range(n - 1, -1, -1):

            for total in range(amount - 1, -1, -1):

                pick = 0

                if total + coins[pos] <= amount:
                    pick = dp[pos][total + coins[pos]]

                no_pick = dp[pos + 1][total]

                dp[pos][total] = pick + no_pick

        return dp[0][0]

    def coinChangeTabulizationOptimization(self, coins, amount):

        n = len(coins)

        dp = [0] * (amount + 1)
        dp[amount] = 1

        for pos in range(n - 1, -1, -1):
            for total in range(amount - 1, -1, -1):

                pick = 0

                if total + coins[pos] <= amount:
                    pick = dp[total + coins[pos]]

                no_pick = dp[total]

                dp[total] = pick + no_pick

        return dp[0]
 

print(Solution().change(amount = 5, coins = [1,2,5]))