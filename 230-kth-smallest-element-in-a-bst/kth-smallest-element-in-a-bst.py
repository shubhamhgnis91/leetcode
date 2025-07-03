# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        inorderTrav = []
        def inorder(root):
            if not root:
                return

            if root.left:
                inorder(root.left)

            inorderTrav.append(root.val)

            if root.right:
                inorder(root.right)


        
        inorder(root)
        
        for num in inorderTrav:
            if k == 1:
                return num

            k -= 1
