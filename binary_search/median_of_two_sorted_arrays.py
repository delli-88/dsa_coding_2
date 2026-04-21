class Solution:
    def findMedianSortedArrays(self, nums1, nums2):

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        low = 0
        high = len(nums1)
        total = len(nums1) + len(nums2)
        req = (total + 1) // 2

        while low <= high:

            mid = (low + high) // 2

            l1 = mid - 1
            l2 = req - mid - 1
            r1 = mid
            r2 = req - mid

            left1  = nums1[l1] if l1 >= 0 else float('-inf')
            left2  = nums2[l2] if l2 >= 0 else float('-inf')
            right1 = nums1[r1] if r1 < len(nums1) else float('inf')
            right2 = nums2[r2] if r2 < len(nums2) else float('inf')

            if left1 <= right2 and left2 <= right1:
                if total % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2
                else:
                    return max(left1, left2)

            elif left1 > right2:
                high = mid - 1
            else:
                low = mid + 1

        return -1

sol = Solution()
print(sol.findMedianSortedArrays(nums1 = [7,12,14,15], nums2 = [1,2,3,4,9,11]))