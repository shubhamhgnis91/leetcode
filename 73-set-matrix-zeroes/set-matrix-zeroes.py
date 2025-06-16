class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        rows = set()
        cols = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        for i in rows:
            matrix[i] = [0] * len(matrix[0])

        for i in range(len(matrix)):
            for j in cols:
                matrix[i][j] = 0