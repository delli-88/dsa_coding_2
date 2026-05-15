from collections import deque
class Solution:
    def isBipartite(self, graph) -> bool:
        
        color = [0] * len(graph)
        for i in range(len(graph)):
            if color[i] == 0 and not self.bfs(graph, i, color):
                return False
        return True

    def bfs(self, graph, node, color):

        queue = deque([node])
        color[node] = 1

        while queue:
            parent = queue.popleft()
            for nei in graph[parent]:
                if color[nei] == 0:
                    color[nei] = -color[parent]
                    queue.append(nei)
                elif color[nei] == color[parent]:
                    return False
        return True

print(Solution().isBipartite([[1,3],[0,2],[1,3],[0,2]]))