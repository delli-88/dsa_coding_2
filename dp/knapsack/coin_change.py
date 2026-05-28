class Solution:
    def coinChange(self, coins, amount):

        dp = [[-1 for _ in range(amount+1)] for _ in range(len(coins))]
        res = self.helper(coins, amount, 0, 0, dp)
        return -1 if res == float("inf") else res

    def helper(self, coins, amount, total, pos, dp):

        if total > amount or pos >= len(coins):
            return float("inf")
        
        if amount == total:
            dp[pos][total] = 0
            return dp[pos][total]

        if dp[pos][total] != -1:
            return dp[pos][total]
        
        pick = 1 + self.helper(coins, amount, total + coins[pos], pos, dp)
        no_pick = self.helper(coins, amount, total, pos+1, dp)
        
        dp[pos][total] = min(pick, no_pick)

        return dp[pos][total]

    def coinChangeTabulization(self, coins, amount):
        n = len(coins)

        dp = [[float("inf") for _ in range(amount + 1)]
              for _ in range(n + 1)]

        for pos in range(n + 1):
            dp[pos][amount] = 0

        for pos in range(n - 1, -1, -1):

            for total in range(amount - 1, -1, -1):

                pick = float("inf")

                if total + coins[pos] <= amount:
                    pick = 1 + dp[pos][total + coins[pos]]

                no_pick = dp[pos + 1][total]

                dp[pos][total] = min(pick, no_pick)

        return dp[0][0] if dp[0][0] != float("inf") else -1

    def coinChangeTabulizationOptimization(self, coins, amount):

        n = len(coins)

        nextOne = [float("inf")] * (amount + 1)
        nextOne[amount] = 0

        for pos in range(n - 1, -1, -1):

            currOne = [float("inf")] * (amount + 1)
            currOne[amount] = 0

            for total in range(amount - 1, -1, -1):

                pick = float("inf")

                if total + coins[pos] <= amount:
                    pick = 1 + currOne[total + coins[pos]]

                no_pick = nextOne[total]

                currOne[total] = min(pick, no_pick)

            nextOne = currOne

        return nextOne[0] if nextOne[0] != float("inf") else -1
    
print(Solution().coinChange(coins = [1,2,5], amount = 11))
print(Solution().coinChangeTabulization(coins = [195,265,404,396], amount = 3239))
print(Solution().coinChangeTabulizationOptimization(coins = [195,265,404,396], amount = 3239))