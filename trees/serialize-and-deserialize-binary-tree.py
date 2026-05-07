from collections import deque
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):

        if not root:
            return ""

        res = []
        queue = deque([root])

        while queue:

            node = queue.popleft()

            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("N")

        return ",".join(res)

    def deserialize(self, data):

        if not data:
            return None

        values = data.split(",")

        root = TreeNode(int(values[0]))
        queue = deque([root])

        i = 1

        while queue:

            node = queue.popleft()

            # left child
            if values[i] != "N":
                node.left = TreeNode(int(values[i]))
                queue.append(node.left)

            i += 1

            # right child
            if values[i] != "N":
                node.right = TreeNode(int(values[i]))
                queue.append(node.right)

            i += 1

        return root
        

# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))