class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map1 = {}
        for i in range(len(nums)):
            if target - nums[i] in map1.keys():
                return [map1[target - nums[i]], i]
            map1[nums[i]] = i
        return [-1,-1]

sol = Solution()
print(sol.twoSum(nums = [2,7,11,15], target = 9))