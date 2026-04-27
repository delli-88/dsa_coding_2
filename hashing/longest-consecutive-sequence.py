class Solution:
    def longestConsecutive(self, nums):
        
        numSet = set(nums)
        maxLen = 0

        for num in numSet:
            if num - 1 not in numSet:
                curr = num
                currLen = 1

                while curr + 1 in numSet:
                    curr += 1
                    currLen += 1

                maxLen = max(maxLen, currLen)

        return maxLen

sol = Solution()
print(sol.longestConsecutive(nums = [100,4,200,1,5,3,2,2]))