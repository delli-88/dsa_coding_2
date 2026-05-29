class Solution:
    def canPartition(self, nums) -> bool:
        numsSum = sum(nums)
        dp = [[None for _ in range(numsSum+1)] for _ in range(len(nums)+1)]
        return self.helper(nums, 0, numsSum, 0, dp)

    def helper(self, nums, pos, numsSum, subset1sum, dp):

        if pos == len(nums):
            if numsSum - subset1sum == subset1sum:
                return True
            return False
        
        if dp[pos][subset1sum]!= None:
            return dp[pos][subset1sum]
        
        inSubset1 = self.helper(nums, pos+1, numsSum, subset1sum+nums[pos], dp)
        inSubset2 = self.helper(nums, pos+1, numsSum, subset1sum, dp)

        dp[pos][subset1sum] = inSubset1 or inSubset2

        return dp[pos][subset1sum]
    
    def canPartitionTabulization(self, nums):
        numsSum = sum(nums)
        dp = [[None for _ in range(numsSum+1)] for _ in range(len(nums)+1)]

        for i in range(numsSum+1):
            if numsSum - i == i:
                dp[-1][i] = True

        for pos in range(len(nums)-1, -1, -1):
            for s in range(numsSum-1, -1, -1):

                inSubset1 = False
                if s + nums[pos] < numsSum:
                    inSubset1 = dp[pos+1][s+nums[pos]]
                inSubset2 = dp[pos+1][s]   

                dp[pos][s] = inSubset1 or inSubset2          

        return dp[0][0] if dp[0][0] in [True, False] else False

    def canPartitionTabulizationOptimization(self, nums):
        numsSum = sum(nums)

        if numsSum % 2 != 0:
            return False

        target = numsSum // 2

        dp = [False for _ in range(target + 1)]

        # Base case
        dp[target] = True

        for pos in range(len(nums) - 1, -1, -1):

            nextDp = dp.copy()

            for subset1sum in range(target - 1, -1, -1):

                inSubset1 = False

                if subset1sum + nums[pos] <= target:
                    inSubset1 = dp[
                        subset1sum + nums[pos]
                    ]

                inSubset2 = dp[subset1sum]

                nextDp[subset1sum] = (
                    inSubset1 or inSubset2
                )

            dp = nextDp

        return dp[0]

print(Solution().canPartition([1,5,11,5]))
print(Solution().canPartitionTabulization([1,5,11,5]))
print(Solution().canPartitionTabulizationOptimization([1,2,5]))