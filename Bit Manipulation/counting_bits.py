class Solution:
    def countBits(self, n):
        res = []

        for i in range(n+1):
            res.append(self.hammingWeight(i))
        
        return res

    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n:
            n &= (n - 1)
            cnt += 1
        return cnt

print(Solution().countBits(5))