class Solution:
    def shipWithinDays(self, weights, days):

        low, high = max(weights), sum(weights)

        while low < high:
            mid = (low + high) // 2

            if self.canShip(weights, days, mid):
                high = mid
            else:
                low = mid + 1

        return low

    def canShip(self, weights, days, capacity):
        days_used = 1
        current_load = 0

        for w in weights:
            if current_load + w <= capacity:
                current_load += w
            else:
                days_used += 1
                current_load = w
                
                if days_used > days:
                    return False

        return True

sol = Solution()
print(sol.shipWithinDays(weights = [1,2,3,1,1], days = 4))