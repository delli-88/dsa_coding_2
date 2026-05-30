class Solution:
    def lastStoneWeightII(self, stones) -> int:
        total = sum(stones)
        dp = [[-1 for _ in range((2*total)+1)] for _ in range(len(stones)+1)]
        return self.helper(stones, 0, 0, total, dp)
    
    def helper(self, nums, pos, sumTill, total, dp):
        
        if pos == len(nums):
            return abs(sumTill)
        
        if dp[pos][total + sumTill]!=-1:
            return dp[pos][total + sumTill]
        
        positive = self.helper(nums, pos+1, sumTill + nums[pos], total, dp)
        negative = self.helper(nums, pos+1, sumTill - nums[pos], total, dp)
        
        dp[pos][total + sumTill] =  min(positive, negative)
        return dp[pos][total + sumTill]

    def lastStoneWeightIITabulization(self, stones):
        numsSum = sum(stones)

        nextRow = [0] * ((2 * numsSum) + 1)

        for s in range(-numsSum, numsSum + 1):
            nextRow[numsSum + s] = abs(s)

        for pos in range(len(stones) - 1, -1, -1):

            curr = [0] * ((2 * numsSum) + 1)

            for s in range(-numsSum, numsSum + 1):

                positive = float("inf")
                negative = float("inf")

                if s + stones[pos] <= numsSum:
                    positive = nextRow[
                        numsSum + (s + stones[pos])
                    ]

                if s - stones[pos] >= -numsSum:
                    negative = nextRow[
                        numsSum + (s - stones[pos])
                    ]

                curr[numsSum + s] = min(
                    positive,
                    negative
                )

            nextRow = curr

        return nextRow[numsSum]

print(Solution().lastStoneWeightII(stones = [2,7,4,1,8,1]))
print(Solution().lastStoneWeightIITabulization(stones = [2,7,4,1,8,1]))