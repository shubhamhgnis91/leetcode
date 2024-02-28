# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack = [root]

        while stack:
            root = stack.pop(0)

            if root.right:
                stack.append(root.right)

            if root.left:
                stack.append(root.left)

        return root.val