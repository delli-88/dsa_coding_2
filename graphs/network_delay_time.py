from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times, n, k):

        adj = defaultdict(list)

        for u, v, w in times:
            adj[u].append((v, w))

        dist = [float("inf")] * (n + 1)
        dist[k] = 0

        heap = [(0, k)]

        while heap:
            currDist, node = heapq.heappop(heap)

            if currDist > dist[node]:
                continue

            for nbr, weight in adj[node]:
                newDist = currDist + weight

                if newDist < dist[nbr]:
                    dist[nbr] = newDist
                    heapq.heappush(heap, (newDist, nbr))

        ans = max(dist[1:])

        return ans if ans != float("inf") else -1

print(Solution().networkDelayTime(times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2))