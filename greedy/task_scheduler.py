import heapq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks, n):
        
        count = Counter(tasks)

        # max heap
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0

        # [remaining_count, next_available_time]
        cooldown = deque()

        while maxHeap or cooldown:

            time += 1

            # execute task
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)

                # still remaining
                if cnt != 0:
                    cooldown.append((cnt, time + n))

            # cooldown finished
            if cooldown and cooldown[0][1] == time:
                heapq.heappush(maxHeap, cooldown.popleft()[0])

        return time


print(Solution().leastInterval(["A","A","A","B","B","B"], 3))