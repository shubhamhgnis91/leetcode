# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        stack, res = [(root, root.val)], 0

        while stack:
            
            node, value = stack.pop(0)

            if not node.right and not node.left:
                res += value

            if node.right:
                stack.append((node.right, value * 10 + node.right.val))

            if node.left:
                stack.append((node.left, value * 10 + node.left.val))

        return res
                

