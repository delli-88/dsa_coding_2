class Solution:
    def maxArea(self, height):

        left = 0
        right = len(height)-1
        maxWater = 0
        while left<right:

            maxWater = max(maxWater, min(height[left], height[right])*(right-left))

            if height[left] < height[right]:
                left+=1
            else:
                right-=1

        return maxWater

sol = Solution()
print(sol.maxArea( height = [1,8,6,2,5,4,8,3,7]))