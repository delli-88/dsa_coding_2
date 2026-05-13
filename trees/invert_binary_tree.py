class Solution:
    def invertTree(self, root):
        
        if root == None:
            return root
        
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        
        root.left = right
        root.right = left

        return root