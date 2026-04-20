class Solution:
    def minEatingSpeed(self, piles, h):

        low = 1
        high = max(piles)

        while low < high:

            mid = (low + high) // 2

            timeTaken = 0
            for i in range(len(piles)):
                
                quo = piles[i]//mid
                rem = piles[i]%mid

                timeTaken += quo + (1 if rem else 0)
            
            if timeTaken > h:
                low = mid + 1
            else:
                high = mid

        return low

sol = Solution()
print(sol.minEatingSpeed(piles = [30,11,23,4,20], h = 6))