class Solution:
    def merge(self, intervals):

        intervals.sort()
        merged = []

        for start, end in intervals:
            if not merged or start > merged[-1][1]:
                merged.append([start, end])
            else:
                merged[-1][1] = max(merged[-1][1], end)

        return merged

sol = Solution()
print(sol.merge(intervals = [[1,4],[2,3]]))