class Solution:
    def lengthOfLIS(self, nums):

        tails = []
        for num in nums:

            left = 0
            right = len(tails) - 1

            # find first element >= num
            while left <= right:
                mid = (left + right) // 2
                if tails[mid] < num:
                    left = mid + 1
                else:
                    right = mid - 1

            # left is insertion/replacement position
            if left == len(tails):
                tails.append(num)
            else:
                tails[left] = num

        return len(tails)


print(Solution().lengthOfLIS([10,9,2,5,3,7,101,18]))