class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:

        for i in range(len(grid)):
            if grid[i][0] == 0:
                for j in range(len(grid[i])):
                    grid[i][j] = 1 - grid[i][j] 

        for j in range(len(grid[0])):
            zero_count = sum(grid[i][j] == 0 for i in range(len(grid)))
            if zero_count > len(grid) / 2:
                for i in range(len(grid)):
                    grid[i][j] = 1 - grid[i][j] 

        score = sum(int(''.join(map(str, row)), 2) for row in grid)
        return score
