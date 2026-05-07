# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.goodNodesHelper(root, -float("inf"))

    def goodNodesHelper(self, root, maxi):

        if root == None:
            return 0
        
        newMax = max(maxi, root.val)

        left = self.goodNodesHelper(root.left, newMax)
        right = self.goodNodesHelper(root.right, newMax)

        good = 1 if root.val >= maxi else 0
        
        return good + left + right