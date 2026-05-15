import heapq

class Solution:
    def minCostConnectPoints(self, points):

        n = len(points)
        minHeap = [(0, 0)]
        visited = set()
        minDist = [float('inf')] * n
        minDist[0] = 0
        totalCost = 0

        while len(visited) < n:
            cost, node = heapq.heappop(minHeap)
            if node in visited:
                continue

            visited.add(node)
            totalCost += cost
            x1, y1 = points[node]

            for nei in range(n):
                if nei in visited:
                    continue

                x2, y2 = points[nei]
                dist = abs(x1 - x2) + abs(y1 - y2)
                if dist < minDist[nei]:
                    minDist[nei] = dist
                    heapq.heappush(minHeap, (dist, nei))

        return totalCost
    
print(Solution().minCostConnectPoints(points = [[0,0],[2,2],[3,10],[5,2],[7,0]]))