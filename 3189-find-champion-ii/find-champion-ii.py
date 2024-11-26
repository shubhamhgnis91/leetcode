class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        
        if n == 1:
            return 0

        in_deg = {}
        
        for edge in edges:
            in_deg[edge[1]] = in_deg.get(edge[1], 0) + 1

        champions = []

        for i in range(n):
            if in_deg.get(i, 0) == 0:
                champions.append(i)

        if len(champions) != 1:
            return -1

        return champions[0]
        