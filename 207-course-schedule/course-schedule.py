class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = collections.defaultdict(list)

        for course in prerequisites:
            adj[course[0]].append(course[1])

        # cycle detect using dfs iterative
        visited = set()
        def dfs(course):
            if not adj[course]:
                return True

            if course in visited:
                return False

            visited.add(course)

            for nei in adj[course]:
                if not dfs(nei):
                    return False

            adj[course] = []
            return True

        
        for i in range(numCourses):
            if not dfs(i):
                return False

        return True

        