class Solution:
    def firstMissingPositive(self, nums) -> int:

        i = 0
        n = len(nums)

        while i < n:
            if 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                correct = nums[i] - 1
                nums[i], nums[correct] = nums[correct], nums[i]
            else:
                i += 1

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1

print(Solution().firstMissingPositive(nums = [0,2,3]))