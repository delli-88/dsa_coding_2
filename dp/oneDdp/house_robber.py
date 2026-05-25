class Solution:
    def rob(self, nums) -> int:
        dp = [-1 for _ in range(len(nums)+1)]
        return self.helper(nums, 0, dp)

    def helper(self, nums, pos, dp):
        if pos >= len(nums):
            return 0
        
        if dp[pos]!=-1:
            return dp[pos]

        include = nums[pos] + self.helper(nums, pos+2, dp)
        exclude = self.helper(nums, pos+1, dp)

        dp[pos] = max(include, exclude)
        return dp[pos]
    
    def robTabulization(self, nums):
        dp = [-1 for _ in range(len(nums))]

        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1])

        dp[-1], dp[-2] = nums[-1], nums[-2]

        for i in range(len(nums)-1, -1, -1):

            include = nums[i] + (dp[i+2] if i+2 < len(nums) else 0)
            exclude = dp[i+1] if i+1 < len(nums) else 0

            dp[i] = max(include, exclude)

        return dp[0]
    
    def robTabulizationOpt(self, nums):

        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        prev1 = 0
        prev2 = 0

        for i in range(len(nums)-1, -1, -1):

            include = nums[i] + (prev2 if i+2 < len(nums) else 0)
            exclude = prev1 if i+1 < len(nums) else 0

            curr = max(include, exclude)
            prev2 = prev1
            prev1 = curr

        return prev1


print(Solution().rob(nums = [2,7,9,3,1]))
print(Solution().robTabulization([2,7,9,3,1]))
print(Solution().robTabulizationOpt([2,7,9,3,1]))