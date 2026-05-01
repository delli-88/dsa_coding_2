class Solution:
    def canCompleteCircuit(self, gas, cost) -> int:

        total = 0
        tank = 0
        start = 0

        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total += diff
            tank += diff
            
            if tank < 0:
                start = i + 1
                tank = 0

        return start if total >= 0 else -1

print(Solution().canCompleteCircuit(gas = [3,1,1], cost = [1,2,2]))