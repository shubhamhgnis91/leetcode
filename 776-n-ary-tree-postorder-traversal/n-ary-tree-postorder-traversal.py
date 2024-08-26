"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        res = []

        if root == None:
            return res

        def po(root):
            if root is not None:
                for child in root.children:
                    po(child)
                res.append(root.val)
        
        po(root)
        return res