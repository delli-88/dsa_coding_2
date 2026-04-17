class Solution:
    def dailyTemperatures(self, temperatures):

        sol = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                topIdx = stack.pop()
                sol[topIdx] = i - topIdx
            stack.append(i)

        return sol

sol = Solution()
print(sol.dailyTemperatures([73,74,75,71,69,72,76,73]))