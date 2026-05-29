class Solution:
    def findTargetSumWays(self, nums, target):
        numsSum = sum(nums)
        dp = [[-1 for _ in range((2*numsSum)+1)] for _ in range(len(nums)+1)]
        return self.helper(nums, target, 0, 0, numsSum, dp)
    
    def helper(self, nums, target, pos, sumTill, total, dp):

        if pos == len(nums):
            if sumTill == target:
                return 1
            return 0
        
        if dp[pos][total + sumTill]!=-1:
            return dp[pos][total + sumTill]
        
        positive = self.helper(nums, target, pos+1, sumTill + nums[pos], total, dp)
        negative = self.helper(nums, target, pos+1, sumTill - nums[pos], total, dp)
        
        dp[pos][total + sumTill] =  positive + negative
        return dp[pos][total + sumTill]
    
    def findTargetSumWaysTabulization(self, nums, target):
        numsSum = sum(nums)

        if abs(target) > numsSum:
            return 0

        dp = [[0 for _ in range((2 * numsSum) + 1)]
            for _ in range(len(nums) + 1)]

        dp[-1][numsSum + target] = 1

        for pos in range(len(nums)-1, -1, -1):
            for s in range(2 * numsSum, -1, -1):

                positive = 0
                if s + nums[pos] <= (2 * numsSum):
                    positive = dp[pos + 1][s + nums[pos]]

                negative = 0
                if s - nums[pos] >= 0:
                    negative = dp[pos + 1][s - nums[pos]]

                dp[pos][s] = positive + negative

        return dp[0][numsSum]
    
    def findTargetSumWaysTabulizationOptimization(self, nums, target):
        numsSum = sum(nums)

        if abs(target) > numsSum:
            return 0

        dp = [0 for _ in range((2 * numsSum) + 1)]

        dp[numsSum + target] = 1

        for pos in range(len(nums)-1, -1, -1):
            dpCopy = dp.copy()
            for s in range(2 * numsSum, -1, -1):

                positive = 0
                if s + nums[pos] <= (2 * numsSum):
                    positive = dp[s + nums[pos]]

                negative = 0
                if s - nums[pos] >= 0:
                    negative = dp[s - nums[pos]]

                dpCopy[s] = positive + negative
            dp = dpCopy[:]

        return dp[numsSum]

print(Solution().findTargetSumWays(nums = [1,1,1,1,1], target = 3))
print(Solution().findTargetSumWaysTabulization(nums = [1,1,1,1,1], target = 3))
print(Solution().findTargetSumWaysTabulizationOptimization(nums = [1,1,1,1,1], target = 3))