class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)

        # transpose
        for r in range(n):
            for c in range(r+1, n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        # reverse
        for row in matrix:
            row.reverse()

        return
    
sol = Solution()
print(sol.rotate(matrix = [[1,2,3],[4,5,6],[7,8,9]]))