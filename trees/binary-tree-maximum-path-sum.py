# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root):
        self.maxi = -float("inf")
        self.dfs(root)
        return self.maxi

    def dfs(self, root):
        if not root:
            return 0

        left = max(0, self.dfs(root.left))
        right = max(0, self.dfs(root.right))

        # best path passing through this node
        self.maxi = max(self.maxi, left + right + root.val)

        # return best single path upward
        return root.val + max(left, right)