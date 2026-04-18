class Solution:
    def largestRectangleArea(self, heights):
        n = len(heights)
        if n == 0:
            return 0

        prevSmaller = [-1] * n
        nextSmaller = [n] * n

        stack = []

        # Previous Smaller
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                prevSmaller[i] = stack[-1]
            stack.append(i)

        stack = []

        # Next Smaller
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                nextSmaller[i] = stack[-1]
            stack.append(i)

        largest = 0

        for i in range(n):
            width = nextSmaller[i] - prevSmaller[i] - 1
            area = heights[i] * width
            largest = max(largest, area)

        return largest

sol = Solution()
print(sol.largestRectangleArea(heights = [2,1,5,6,2,3]))