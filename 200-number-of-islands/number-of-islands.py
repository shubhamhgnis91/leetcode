class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        res = 0

        def dfs(row, col):
            q = deque()
            visited.add((row, col))
            q.append((row, col))

            while q:
                r, c = q.popleft()
                neighbours = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]

                for x, y in neighbours:
                    if x in range(rows) and y in range(cols) and grid[x][y] == "1" and (x, y) not in visited:
                        q.append((x, y))
                        visited.add((x, y))



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    dfs(r, c)
                    res += 1

        return res