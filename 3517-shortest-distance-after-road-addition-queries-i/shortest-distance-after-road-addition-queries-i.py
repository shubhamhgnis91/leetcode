from collections import deque

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:

        adjacency_list = {i: [] for i in range(n)}
        for i in range(n - 1):
            adjacency_list[i].append(i + 1)

        def bfs():
            queue = deque([0])
            visited = set()
            distance = {0: 0}

            while queue:
                current = queue.popleft()
                if current == n - 1:
                    return distance[current]

                for neighbour in adjacency_list[current]:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        queue.append(neighbour)
                        distance[neighbour] = distance[current] + 1
            
            return -1

        res = []

        for u, v in queries:
            adjacency_list[u].append(v)
            res.append(bfs())

        return res
