class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        
        inorderMap = {}
        for i, val in enumerate(inorder):
            inorderMap[val] = i

        def helper(preStart, preEnd, inStart, inEnd):

            if preStart > preEnd or inStart > inEnd:
                return None

            rootVal = preorder[preStart]
            root = TreeNode(rootVal)

            rootIndex = inorderMap[rootVal]

            leftSize = rootIndex - inStart

            root.left = helper(
                preStart + 1,
                preStart + leftSize,
                inStart,
                rootIndex - 1
            )

            root.right = helper(
                preStart + leftSize + 1,
                preEnd,
                rootIndex + 1,
                inEnd
            )

            return root

        n = len(preorder)

        return helper(0, n - 1, 0, n - 1)
        
