class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        
        sol = []
        self.helper(nums, 0, [], sol)
        return sol
    
    def helper(self, nums, pos, subset, sol):

        sol.append(subset[:])

        for i in range(pos, len(nums)):

            # skip duplicates at same recursion level
            if i > pos and nums[i] == nums[i-1]:
                continue

            subset.append(nums[i])
            self.helper(nums, i+1, subset, sol)
            subset.pop()
            
print(Solution().subsetsWithDup(nums = [1,2,2,2,3]))