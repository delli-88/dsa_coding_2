class Solution:
    def maxDepth(self, root):
        maxi = [0]
        self.maxDepthHelper(root, 0, maxi)
        return maxi[0]
    
    def maxDepthHelper(self, root, height, maxi):
        
        if root == None:
            return
        maxi[0] = max(maxi[0], height+1)
        self.maxDepthHelper(root.left, height+1, maxi)
        self.maxDepthHelper(root.right, height+1, maxi)

        return