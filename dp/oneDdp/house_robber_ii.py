import house_robber
class Solution:
    def rob(self, nums):
        sol = house_robber.Solution()
        if len(nums)<=3:
            return max(nums)
        rob1 = sol.robTabulizationOpt(nums[1:])
        rob2 = sol.robTabulizationOpt(nums[:len(nums)-1])
        return max(rob1, rob2)

print(Solution().rob([1,2,3,1]))