class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0

        visited = set()
        res = 0
        rows, cols = len(grid), len(grid[0])


        def dfs(row, col):
            q = deque()
            visited.add((row, col))
            q.append((row, col))

            while q:
                r, c = q.popleft()
                neighbours = [[r, c - 1], [r, c + 1], [r + 1, c], [r - 1, c]]

                for x, y in neighbours:
                    if x in range(rows) and y in range(cols) and grid[x][y] == "1" and (x, y) not in visited:
                        visited.add((x, y))
                        q.append((x, y))

        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visited:
                    dfs(i, j)
                    res += 1


        return res



