class Solution:
    def jump(self, nums):
        
        steps = 0
        left = right = 0

        while right < len(nums) - 1:
            farthest = 0
            
            for i in range(left, right + 1):
                farthest = max(farthest, i + nums[i])
            
            left = right + 1
            right = farthest
            steps += 1

        return steps

    
print(Solution().jump(nums = [2,3,1,1,4]))