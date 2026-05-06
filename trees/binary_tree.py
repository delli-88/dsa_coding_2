class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self):
        return str(self.__dict__)
    
class BinaryTree:
    def __init__(self, arr):
        self.root = self.build_tree(arr)
    
    def __str__(self):
        return str(self.__dict__)

    def build_tree(self, arr):
        if not arr:
            return None

        root = TreeNode(arr[0])
        queue = [root]
        i = 1

        while queue and i < len(arr):
            current = queue.pop(0)

            if current:
                # Left child
                if i < len(arr) and arr[i] is not None:
                    current.left = TreeNode(arr[i])
                    queue.append(current.left)
                i += 1

                # Right child
                if i < len(arr) and arr[i] is not None:
                    current.right = TreeNode(arr[i])
                    queue.append(current.right)
                i += 1

        return root
    

print(BinaryTree([3,5,1,6,2,0,8,None,None,7,4]))