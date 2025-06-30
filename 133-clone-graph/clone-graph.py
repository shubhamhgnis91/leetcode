"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        mp = {}
        
        def bfs(node):
            q = deque([node])
            mp[node] = Node(node.val)

            while q:
                n = q.popleft()
                for neigh in n.neighbors:
                    if neigh not in mp:
                        mp[neigh] = Node(neigh.val)
                        q.append(neigh)
                    mp[n].neighbors.append(mp[neigh])

        
        bfs(node)
        return mp[node]

