# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

  
class Solution(object):
    li=""       

    def trav(self,root):
        if root is None:
            return
        self.li+=str(root.val)

        if root.left is not None:
            self.li+="("
            self.trav(root.left)
            self.li+=")"

        if root.right is not None:
            if root.left is None:
                self.li+="()"
            self.li+="("
            self.trav(root.right)
            self.li+=")"

    def tree2str(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """        
        self.trav(root)
        return self.li