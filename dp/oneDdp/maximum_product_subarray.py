class Solution:

    def maxProduct(self, nums):

        maxi = [-float("inf")]

        self.helper(nums, 0, maxi)

        return maxi[0]

    def helper(self, nums, pos, maxi):

        if pos == len(nums):
            return (1, 1)

        next_max, next_min = self.helper(nums, pos + 1, maxi)

        extend_max = nums[pos] * next_max
        extend_min = nums[pos] * next_min

        cur_max = max(nums[pos], extend_max, extend_min)
        cur_min = min(nums[pos], extend_max, extend_min)

        maxi[0] = max(maxi[0], cur_max)

        return (cur_max, cur_min)

    def maxProductTabulation(self, nums):

        maxi = -float("inf")
        dp = [-1 for _ in range(len(nums)+1)]
        dp[-1] = (1,1)

        for pos in range(len(nums)-1, -1, -1):

            next_max, next_min = dp[pos + 1]
            extend_max = nums[pos] * next_max
            extend_min = nums[pos] * next_min
            cur_max = max(nums[pos], extend_max, extend_min)
            cur_min = min(nums[pos], extend_max, extend_min)
            maxi = max(maxi, cur_max)
            dp[pos] = (cur_max, cur_min)

        return maxi

    def maxProductTabulationSpaceOpt(self, nums):

        maxi = -float("inf")
        last = (1,1)

        for pos in range(len(nums)-1, -1, -1):

            next_max, next_min = last
            extend_max = nums[pos] * next_max
            extend_min = nums[pos] * next_min
            cur_max = max(nums[pos], extend_max, extend_min)
            cur_min = min(nums[pos], extend_max, extend_min)
            maxi = max(maxi, cur_max)
            last = (cur_max, cur_min)

        return maxi

print(Solution().maxProduct([-1,-2,2,4,-3,2]))
print(Solution().maxProductTabulation(nums = [-1,-2,2,4,-3,2]))