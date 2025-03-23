class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        mod = 10**9 + 7
        
        graph = defaultdict(list)
        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))  

        distances = [float('inf')] * n
        ways = [0] * n
        distances[0] = 0
        ways[0] = 1

        heap = [(0, 0)]  

        while heap:
            cur_dist, u = heapq.heappop(heap)
            if cur_dist > distances[u]:
                continue

            for v, time in graph[u]:
                new_dist = cur_dist + time
                
                if new_dist < distances[v]:
                    distances[v] = new_dist
                    ways[v] = ways[u]
                    heapq.heappush(heap, (new_dist, v))
                
                elif new_dist == distances[v]:
                    ways[v] = (ways[v] + ways[u]) % mod

        return ways[n-1]