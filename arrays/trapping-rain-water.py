class Solution:
    def trap(self, height) -> int:

        waterTrapped = 0
        left = 0
        right = len(height)-1
        leftMax = height[left]
        rightMax = height[right]

        while left < right:

            if height[left] < height[right]:
                if leftMax > height[left]:
                    waterTrapped += leftMax - height[left]
                else:
                    leftMax = height[left]
                left += 1
            else:
                if rightMax > height[right]:
                    waterTrapped += rightMax - height[right]
                else:
                    rightMax = height[right]
                right -= 1

        return waterTrapped

print(Solution().trap(height = [0,1,0,2,1,0,1,3,2,1,2,1]))