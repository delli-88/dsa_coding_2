import heapq
from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):

        adj = defaultdict(list)

        for u, v, w in flights:
            adj[u].append((v, w))

        heap = [(0, src, 0)]

        dist = [[float("inf")] * (k + 2) for _ in range(n)]
        dist[src][0] = 0

        while heap:
            cost, node, stops = heapq.heappop(heap)

            if node == dst:
                return cost

            if stops == k + 1:
                continue

            for nei, price in adj[node]:

                newCost = cost + price

                if newCost < dist[nei][stops + 1]:
                    dist[nei][stops + 1] = newCost
                    heapq.heappush(heap, (newCost, nei, stops + 1))

        return -1

print(Solution().findCheapestPrice(n = 5, flights = [[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]], src = 0, dst = 2, k = 3))