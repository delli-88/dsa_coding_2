class Solution:
    def singleNumber(self, nums) -> int:
        ans = 0
        for num in nums:
            ans ^= num
        return ans

print(Solution().singleNumber(nums = [2,2,1,1,5,6,5]))