class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        low, mid = 0, 0
        high = len(nums)-1

        while mid< len(nums) and mid <= high:

            if nums[mid]==0:
                nums[low], nums[mid] = nums[mid], nums[low]
                mid+=1
                low+=1
            elif nums[mid]==2:
                nums[high], nums[mid] = nums[mid], nums[high]
                high-=1
            else:
                mid+=1
        return

sol = Solution()
print(sol.sortColors([2,0,2,1,1,0]))