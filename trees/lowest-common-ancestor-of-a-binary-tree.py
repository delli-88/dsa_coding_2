class Solution:
    def lowestCommonAncestor(self, root, p, q):
        return self.lowestCommonAncestorHelper(root, p, q)

    def lowestCommonAncestorHelper(self, root, p, q):

        if root == None:
            return None
        
        if root == p or root == q:
            return root
        
        left = self.lowestCommonAncestorHelper(root.left, p, q)
        right = self.lowestCommonAncestorHelper(root.right, p, q)

        if left and right:
            return root
        
        return left or right