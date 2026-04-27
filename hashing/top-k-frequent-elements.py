class Solution:
    def topKFrequent(self, nums, k):

        freqMap = {}
        for num in nums:
            freqMap[num] = freqMap.get(num, 0) + 1
        
        buckets = [[] for _ in range(len(nums)+1)]
        for key,val in freqMap.items():
            buckets[val].append(key)

        topK = []
        for bucket in range(len(buckets)-1, -1, -1):
            for idx in range(len(buckets[bucket])):
                topK.append(buckets[bucket][idx])
                if len(topK)==k:
                    return topK
        return topK


sol = Solution()
print(sol.topKFrequent(nums = [1,1,1,2,2,2,3,3,3], k = 2))