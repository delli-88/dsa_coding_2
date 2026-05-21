class Solution:
    def myPow(self, x: float, n: int) -> float:

        if x == 0:
            return 1
        
        if x == 1:
            return x

        return x * pow(x, n-1)

print(Solution().myPow(x = 2.00000, n = 10))