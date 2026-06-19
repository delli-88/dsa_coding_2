class Solution:
    def subarraySum(self, nums, k):

        hashMap = {}
        hashMap[0] = 1
        prefixSum = 0
        counter = 0

        for i in range(len(nums)):

            prefixSum += nums[i]
            if prefixSum - k in hashMap:
                counter += hashMap[prefixSum - k]
            hashMap[prefixSum] = hashMap.get(prefixSum, 0) + 1
        return counter
    
print(Solution().subarraySum(nums = [1, -1, 1, -1], k = 0))