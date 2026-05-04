class Solution:
    def diameterOfBinaryTree(self, root):
        return self.diameterOfBinaryTreeHelper(root)[1]

    def diameterOfBinaryTreeHelper(self, root):

        if root is None:
            return (0, 0)
        
        left_h, left_d = self.diameterOfBinaryTreeHelper(root.left)
        right_h, right_d = self.diameterOfBinaryTreeHelper(root.right)

        height = 1 + max(left_h, right_h)
        through_root = left_h + right_h
        diameter = max(through_root, left_d, right_d)

        return (height, diameter)
