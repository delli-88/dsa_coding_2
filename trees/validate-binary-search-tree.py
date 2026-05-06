class Solution:
    def isValidBST(self, root) -> bool:
        return self.isValidBSTHelper(root, -float("inf"), float("inf"))
    
    def isValidBSTHelper(self, root, leftRange, rightRange):

        if root == None:
            return True
        
        if not (leftRange < root.val < rightRange):
            return False
        
        leftSubTree = self.isValidBSTHelper(root.left, leftRange, root.val)
        rightSubTree = self.isValidBSTHelper(root.right, root.val, rightRange)

        return leftSubTree and rightSubTree