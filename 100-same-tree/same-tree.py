# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        queue = deque()
        queue.append((p, q))

        while queue:
            x, y = queue.popleft()

            if not x and not y:
                continue

            if (x is not None and y is None) or (x is None and y is not None) or (x.val != y.val):
                return False
                
            queue.append((x.left, y.left))            
            queue.append((x.right, y.right))

            

        return True