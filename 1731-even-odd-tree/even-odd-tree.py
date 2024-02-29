# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isEvenOddTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack = [root]
        level = 0

        while stack:
            prev = None

            for _ in range(len(stack)):
                root = stack.pop(0)

                if level % 2 == 0:
                    if root.val % 2 == 0:
                        return False

                    if prev is not None and prev.val >= root.val:
                        return False
                
                else:
                    if root.val % 2 != 0:
                        return False

                    if prev is not None and prev.val <= root.val:
                        return False


                if root.left:
                    stack.append(root.left)                

                if root.right:
                    stack.append(root.right)

                prev = root

            level += 1

        return True