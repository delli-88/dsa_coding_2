class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self):
        return str(self.__dict__)
    

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.numOfNodes = 0

    def __str__(self):
        return str(self.__dict__)
        
    def insert (self, val):

        newNode = TreeNode(val)

        if not self.root:
            self.root = newNode
            self.numOfNodes += 1
            return
        
        currNode = self.root

        while True:
            if val < currNode.val:
                if currNode.left:
                    currNode = currNode.left
                else:
                    currNode.left = newNode
                    break
            else:
                if currNode.right:
                    currNode = currNode.right
                else:
                    currNode.right = newNode
                    break
        
        self.numOfNodes += 1
        
        return

    def search(self, val):

        currNode = self.root

        while currNode:

            if currNode.val == val:
                return True
            
            if val < currNode.val:
                currNode = currNode.left
            else:
                currNode = currNode.right
        
        return False
    
    def delete(self, val):
        parent = None
        curr = self.root

        while curr and curr.val != val:
            parent = curr
            if val < curr.val:
                curr = curr.left
            else:
                curr = curr.right

        if not curr:
            return None

        if not curr.left or not curr.right:
            child = curr.left if curr.left else curr.right

            if not parent:
                self.root = child
            elif parent.left == curr:
                parent.left = child
            else:
                parent.right = child

        else:
            succ_parent = curr
            succ = curr.right

            while succ.left:
                succ_parent = succ
                succ = succ.left

            curr.val = succ.val

            if succ_parent.left == succ:
                succ_parent.left = succ.right
            else:
                succ_parent.right = succ.right

        self.numOfNodes -= 1
        return True