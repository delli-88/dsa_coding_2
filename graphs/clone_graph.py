from collections import deque
from typing import Optional

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node):
        if not node:
            return None

        nodeMap = {node: Node(node.val)}

        queue = deque([node])

        while queue:
            curr = queue.popleft()

            for neighbor in curr.neighbors:

                # create clone if not seen
                if neighbor not in nodeMap:
                    nodeMap[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)

                # connect cloned nodes
                nodeMap[curr].neighbors.append(nodeMap[neighbor])

        return nodeMap[node]