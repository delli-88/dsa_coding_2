from collections import defaultdict
class Solution:

    def findItinerary(self, tickets):
        adjList = defaultdict(list)
        for src, dst in sorted(tickets, reverse=True):
            adjList[src].append(dst)

        sol = []

        def dfs(node):
            while adjList[node]:
                nei = adjList[node].pop()
                dfs(nei)
            sol.append(node)

        dfs("JFK")

        return sol[::-1]

print(Solution().findItinerary(tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))