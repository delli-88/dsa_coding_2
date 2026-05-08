class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class NumArray:

    def __init__(self, nums):
        self.length = len(nums)
        self.nums = nums
        self.segmentTree = self.buildSegmentTree(nums, 0, len(nums))

    def update(self, index: int, val: int) -> None:
        self.updateSegmentTree(index, val, self.segmentTree, 0, self.length-1)
        return

    def sumRange(self, left: int, right: int) -> int:
        return self.rangeSegmentTree(left, right, self.segmentTree, 0, self.length)
    
    def buildSegmentTree(self, nums, start, end):

        if start > end:
            return None
        
        if start == end:
            return TreeNode(nums[start])

        mid = (end - start) // 2
        left = self.buildSegmentTree(nums, start, mid)
        right = self.buildSegmentTree(nums, mid + 1, end)

        leftVal = left.val if left.val else 0
        rightVal = right.val if right.val else 0

        rootNode = TreeNode(leftVal + rightVal)
        rootNode.left = left
        rootNode.right = right

        return rootNode
    
    def updateSegmentTree(self, index, val, root, start, end):

        if start > end:
            return 0
        
        if start == end:
            if index == start:
                root.val = val
                return val
            else:
                return root.val
        
        mid = (end - start) // 2
        left = root.left.val if root.left else 0
        right = root.right.val if root.right else 0
        if index<=mid:
            left = self.updateSegmentTree(index, val, root.left, start, mid)
        else:
            right = self.updateSegmentTree(index, val, root.right, mid+1, end)
        
        root.val = left + right

        return root.val
    
    def rangeSegmentTree(self, left, right, root, start, end):

        if start > end:
            return 0
        
        if start == left and end == right:
            return root.val
        
        mid = (start + end) // 2
        left = 0
        right = 0
        if end<=mid:
            left = self.updateSegmentTree(left, right, root.left, start, mid)
        elif start > mid:
            right = self.updateSegmentTree(left, right, root.right, mid+1, end)
        else:
            left = self.updateSegmentTree(left, right, root.left, start, mid)
            right = self.updateSegmentTree(left, right, root.right, mid+1, end)     
        
        return left + right








# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)