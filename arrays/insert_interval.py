class Solution:
    def insert(self, intervals, newInterval):
        result = []
        i = 0
        n = len(intervals)

        # Phase 1: add all intervals before newInterval
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # Phase 2: merge overlapping intervals
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        result.append(newInterval)

        # Phase 3: add remaining intervals
        while i < n:
            result.append(intervals[i])
            i += 1

        return result

sol = Solution()
print(sol.insert(intervals = [[1,3],[6,9]], newInterval = [2,5]))