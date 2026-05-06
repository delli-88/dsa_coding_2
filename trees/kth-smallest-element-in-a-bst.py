class Solution:
    def kthSmallest(self, root, k):
        def inorder(node):
            nonlocal k
            
            if not node:
                return None
            
            # Traverse left
            left = inorder(node.left)
            if left is not None:
                return left
            
            # Visit current node
            k -= 1
            if k == 0:
                return node.val
            
            # Traverse right
            return inorder(node.right)
        
        return inorder(root)
