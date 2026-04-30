class Solution:
    def findDisappearedNumbers(self, nums):

        i = 0
        while i < len(nums):
            correct = nums[i] - 1
            if nums[i] != nums[correct]:
                nums[i], nums[correct] = nums[correct], nums[i]
            else:
                i += 1

        sol = []
        for i in range(len(nums)):
            if nums[i] != i + 1:
                sol.append(i + 1)

        return sol

print(Solution().findDisappearedNumbers(nums = [4,3,2,7,8,2,3,1]))