class Solution:
    def maxSubArray(self, nums):

        max_sum = nums[0]
        max_till_now = nums[0]

        for i in range(1, len(nums)):
            max_till_now = max(nums[i], max_till_now + nums[i])
            max_sum = max(max_sum, max_till_now)
        return max_sum

sol = Solution()
print(sol.maxSubArray(nums = [-2,1,-3,4,-1,2,1,-5,4]))