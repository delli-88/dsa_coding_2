from union_find import UnionFind
class Solution:
    def findRedundantConnection(self, edges):

        unionFind = UnionFind(len(edges)+1)
        for node1, node2 in edges:
            if unionFind.findParent(node1) == unionFind.findParent(node2):
                return [node1, node2]
            unionFind.union(node1, node2)

        return [-1, -1]
    
print(Solution().findRedundantConnection(edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]))