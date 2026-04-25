class Solution:
    def eraseOverlapIntervals(self, intervals):

        if len(intervals) == 0:
            return 0
        
        intervals = sorted(intervals, key=lambda x:x[1])
        prev_end = intervals[0][1]
        count = 0

        for i in range(1, len(intervals)):

            start = intervals[i][0]
            end = intervals[i][1]

            if start < prev_end:
                count += 1
            else:
                prev_end = end

        return count

sol = Solution()
print(sol.eraseOverlapIntervals(intervals = [[1,2],[1,2],[1,2]]))