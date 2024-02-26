# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def isSame(p, q):
            if (p is None and q is not None) or (q is None and p is not None):
                return False
            
            if p is None and q is None:
                return True
            
            return p.val == q.val and isSame(p.left, q.left) and isSame(p.right, q.right)

        return isSame(p, q)