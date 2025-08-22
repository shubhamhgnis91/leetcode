class Solution:
    def minimumArea(self, matrix: List[List[int]]) -> int:
        
        n, m = len(matrix), len(matrix[0])
    
        top = n
        bottom = -1
        left = m
        right = -1

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 1:
                    top = min(top, i)
                    bottom = max(bottom, i)
                    left = min(left, j)
                    right = max(right, j)

        # No 1s found
        if bottom == -1:
            return 0  

        height = bottom - top + 1
        width = right - left + 1

        return height * width
                    

        

