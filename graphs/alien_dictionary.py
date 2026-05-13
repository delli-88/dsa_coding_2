from collections import defaultdict, deque

class Solution:
    def findOrder(self, words):

        # Initialize graph
        graph = defaultdict(set)
        indegree = {c: 0 for word in words for c in word}

        # Build graph
        for i in range(len(words) - 1):

            w1, w2 = words[i], words[i + 1]

            # Invalid prefix case
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""

            # Find first differing character
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    if c2 not in graph[c1]:
                        graph[c1].add(c2)
                        indegree[c2] += 1
                    break

        # Topological sort
        queue = deque([c for c in indegree if indegree[c] == 0])
        order = []

        while queue:
            char = queue.popleft()
            order.append(char)

            for neighbor in graph[char]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # Cycle detection
        return "".join(order) if len(order) == len(indegree) else ""


print(Solution().findOrder(words = ["baa", "abcd", "abca", "cab", "cad"]))