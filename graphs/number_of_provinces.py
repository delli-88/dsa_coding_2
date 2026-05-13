class Solution:
    def findCircleNum(self, isConnected) -> int:

        n = len(isConnected)
        visited = set()
        provinces = 0

        for node in range(n):
            if node not in visited:
                self.dfs(isConnected, visited, node)
                provinces += 1

        return provinces

    def dfs(self, graph, visited, node):
        visited.add(node)

        for neighbor in range(len(graph[node])):
            if graph[node][neighbor] == 1 and neighbor not in visited:
                self.dfs(graph, visited, neighbor)

print(Solution().findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))