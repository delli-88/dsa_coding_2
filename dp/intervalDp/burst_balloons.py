class Solution:
    def maxCoins(self, nums:list):
        nums.insert(0, 1)
        nums.append(1)
        dp = [[-1 for _ in range(len(nums))] for _ in range(len(nums))]
        return self.helper(nums, 0, len(nums)-1, dp)
    
    def helper(self, nums, left, right, dp):

        if right - left  == 1:
            return 0
        
        if dp[left][right] != -1:
            return dp[left][right]
        
        maxi = 0
        
        for k in range(left+1, right):
            res = self.helper(nums, left, k, dp) + self.helper(nums, k, right, dp) + (nums[left] * nums[k] * nums[right])
            maxi = max(maxi, res)

        dp[left][right] = maxi

        return dp[left][right]

print(Solution().maxCoins(nums = [3,1,5,8]))