class Solution:
    def missingNumber(self, nums) -> int:
        xor = len(nums)
        for i in range(len(nums)):
            xor ^= i ^ nums[i]
        return xor
    
print(Solution().missingNumber( [8,6,4,2,3,5,7,0,1]))