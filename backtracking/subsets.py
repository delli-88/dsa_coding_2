class Solution:
    def subsets(self, nums):
        sol = []
        self.backtrack(nums, 0, [], sol)
        return sol
    
    def backtrack(self, nums, idx, subSet, sol):
        if idx == len(nums):
            sol.append(subSet[:])
            return
        
        
        subSet.append(nums[idx])
        self.backtrack(nums, idx+1, subSet, sol)

        subSet.pop()
        self.backtrack(nums, idx+1, subSet, sol)

        return

print(Solution().subsets(nums = [1,2,3]))