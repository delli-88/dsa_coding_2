class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)
        m = len(matrix[0])

        fillRowsWithZero = False
        for i in range(m):
            if matrix[0][i] == 0:
                fillRowsWithZero = True
            
        fillColsWithZero = False
        for j in range(n):
            if matrix[j][0] == 0:
                fillColsWithZero = True
        
        for r in range(1, n):
            for c in range(1, m):
                if matrix[r][c]==0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0
        
        for row in range(1,n):
            for col in range(1,m):
                if matrix[0][col]==0 or matrix[row][0]==0:
                    matrix[row][col] = 0
        
        if fillRowsWithZero:
            for i in range(m):
                matrix[0][i] = 0
            
        if fillColsWithZero:
            for j in range(n):
                matrix[j][0] = 0

        print(matrix)
        return


sol = Solution()
print(sol.setZeroes(matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]))