class Solution:    
    def maxProfit(self, prices):

        min_till_now = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            if prices[i]< min_till_now:
                min_till_now = prices[i]
            else:
                max_profit = max(max_profit, prices[i]-min_till_now)
        return max_profit

sol = Solution()
print(sol.maxProfit(prices = [7,1,5,3,6,4]))