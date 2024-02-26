# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def isSymm(p, q):
            
            if (p is None and q is not None) or (q is None and p is not None):
                return False
            
            if p is None and q is None:
                return True

            return p.val == q.val and isSymm(p.left, q.right) and isSymm(p.right, q.left) 
        
        if root is None:
            return True
        
        return isSymm(root.left, root.right)