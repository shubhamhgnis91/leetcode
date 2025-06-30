class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        if not grid:
            return 0

        res = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def bfs(row, col):
            q = deque()
            q.append((row, col))
            visited.add((row, col))
            
            area = 1
            while q:
                r, c = q.popleft()
                
                neighbours = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]
                for x, y in neighbours:
                    if x in range(rows) and y in range(cols) and grid[x][y] == 1 and (x, y) not in visited:
                        visited.add((x, y))
                        q.append((x, y))
                        area += 1
                        

            return area


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    area = bfs(r, c)
                    res = max(res, area)

        return res
                   