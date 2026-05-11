class Graph:

    def __init__(self):
        self.nodeCount = 0
        self.adjacencyList = {}
    
    def __str__(self):
        return str(self.__dict__)

    def addVertex(self, node):

        if node in self.adjacencyList:
            print("Already added")
            return
        
        self.adjacencyList[node] = []
        self.nodeCount += 1
        return

    def addEdge(self, node1, node2):

        if node1 not in self.adjacencyList:
            self.addVertex(node1)
        
        if node2 not in self.adjacencyList:
            self.addVertex(node2)
        
        if node2 not in self.adjacencyList[node1] and node1 not in self.adjacencyList[node2]:        
            self.adjacencyList[node1].append(node2)
            self.adjacencyList[node2].append(node1)
        else:
            print("edge already added")

        return

myGraph = Graph()
myGraph.addVertex(0)
myGraph.addVertex(1)
myGraph.addVertex(2)
myGraph.addVertex(3)
myGraph.addEdge(0,2)
myGraph.addEdge(1,2)
myGraph.addEdge(3,2)
myGraph.addEdge(1,3)
print(myGraph)