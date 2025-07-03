# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        
        def inorder(root):
            nonlocal ans, cnt
            if not root:
                return
            
            inorder(root.left)

            cnt += 1
            if cnt == k:
                ans = root.val
                return                

            inorder(root.right)


        ans = 0
        cnt = 0
        inorder(root)
        
        return ans
