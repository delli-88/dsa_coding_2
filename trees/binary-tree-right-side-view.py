from collections import deque
class Solution:
    def rightSideView(self, root):
        if not root:
            return []
        
        res = []
        queue = deque([root])

        while queue:
            
            currLevelLen = len(queue)
            for i in range(currLevelLen):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
                if i==currLevelLen-1:
                    res.append(node.val)
        
        return res