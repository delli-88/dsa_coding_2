class Solution:
    def findMinArrowShots(self, points):
        
        points.sort(key=lambda x: x[0])

        arrows = 1
        current_end = points[0][1]

        for start, end in points[1:]:

            if start <= current_end:
                current_end = min(current_end, end)

            else:
                arrows += 1
                current_end = end

        return arrows

print(Solution().findMinArrowShots(points = [[1,2],[2,3],[3,4],[4,5]]))