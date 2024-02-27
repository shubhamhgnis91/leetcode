# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    ans = 0
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dia(root):
            if root is None:
                return 0

            left = dia(root.left)
            right = dia(root.right)

            self.ans = max(self.ans, left + right)
            return 1 + max(left, right)
        
        dia(root)
        return self.ans