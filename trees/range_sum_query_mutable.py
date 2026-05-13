class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class NumArray:

    def __init__(self, nums):
        self.n = len(nums)
        self.root = self.build(nums, 0, self.n - 1)

    def build(self, nums, start, end):

        if start > end:
            return None

        if start == end:
            return TreeNode(nums[start])

        mid = (start + end) // 2

        left = self.build(nums, start, mid)
        right = self.build(nums, mid + 1, end)

        root = TreeNode(left.val + right.val)
        root.left = left
        root.right = right

        return root

    def update(self, index, val):
        self.updateTree(self.root, 0, self.n - 1, index, val)

    def updateTree(self, node, start, end, index, val):

        if start == end:
            node.val = val
            return

        mid = (start + end) // 2

        if index <= mid:
            self.updateTree(node.left, start, mid, index, val)
        else:
            self.updateTree(node.right, mid + 1, end, index, val)

        node.val = node.left.val + node.right.val

    def sumRange(self, left, right):
        return self.query(self.root, 0, self.n - 1, left, right)

    def query(self, node, start, end, left, right):

        if left == start and right == end:
            return node.val

        mid = (start + end) // 2

        if right <= mid:
            return self.query(node.left, start, mid, left, right)

        elif left > mid:
            return self.query(node.right, mid + 1, end, left, right)

        else:
            return (
                self.query(node.left, start, mid, left, mid)
                + self.query(node.right, mid + 1, end, mid + 1, right)
            )