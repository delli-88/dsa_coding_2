class Solution:
    def permute(self, nums):
        sol = []
        self.backtrack(nums, 0, sol)
        return sol
    
    def backtrack(self, nums, pos, sol):

        if pos==len(nums):
            sol.append(nums[:])
            return

        for i in range(pos, len(nums)):
            nums[pos], nums[i] = nums[i], nums[pos]
            self.backtrack(nums, pos+1, sol)
            nums[pos], nums[i] = nums[i], nums[pos]

        return

print(Solution().permute(nums = [1,2,3]))