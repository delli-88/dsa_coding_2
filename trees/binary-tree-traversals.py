class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode):
        sol = []
        return self.inorderTraversalHelper(root, sol)
    
    def inorderTraversalHelper(self, root, sol):
        if root == None:
            return sol
        
        self.inorderTraversalHelper(root.left, sol)
        sol.append(root.val)
        self.inorderTraversalHelper(root.right, sol)

        return sol
    
    def inorderTraversalIterative(self, root):
        sol = []
        stack = []
        curr = root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            sol.append(curr.val)
            curr = curr.right

        return sol

    def preorderTraversal(self, root: TreeNode):
        sol = []
        return self.preorderTraversalHelper(root, sol)
    
    def preorderTraversalHelper(self, root, sol):
        if root == None:
            return sol
        
        sol.append(root.val)
        self.preorderTraversalHelper(root.left, sol)
        self.preorderTraversalHelper(root.right, sol)

        return sol
    
    def preorderTraversalIterative(self, root):
        sol = []
        stack = []
        curr = root

        while stack or curr:

            while curr:
                sol.append(curr.val)
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            curr = curr.right

        return sol

    def postorderTraversal(self, root: TreeNode):
        sol = []
        return self.postorderTraversalHelper(root, sol)
    
    def postorderTraversalHelper(self, root, sol):
        if root == None:
            return sol
        
        self.preorderTraversalHelper(root.left, sol)
        self.preorderTraversalHelper(root.right, sol)
        sol.append(root.val)

        return sol
    
    def postorderTraversalIterative(self, root):
        sol = []
        stack = []
        curr = root
        last_visited = None

        while stack or curr:
            # go left as much as possible
            while curr:
                stack.append(curr)
                curr = curr.left

            peek = stack[-1]

            # if right exists and not processed yet → go right
            if peek.right and last_visited != peek.right:
                curr = peek.right
            else:
                sol.append(peek.val)
                last_visited = stack.pop()

        return sol