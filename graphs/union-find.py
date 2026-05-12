class UnionFind:
    def __init__(self, size):
        self.size = [1] * size
        self.parent = [i for i in range(size)]

    def __str__(self):
        return str(self.__dict__)

    def findParent(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.findParent(self.parent[node])

        return self.parent[node]

    def union(self, node1, node2):
        parent1 = self.findParent(node1)
        parent2 = self.findParent(node2)

        if parent1 == parent2:
            return

        if self.size[parent1] >= self.size[parent2]:
            self.parent[parent2] = parent1
            self.size[parent1] += self.size[parent2]
        else:
            self.parent[parent1] = parent2
            self.size[parent2] += self.size[parent1]