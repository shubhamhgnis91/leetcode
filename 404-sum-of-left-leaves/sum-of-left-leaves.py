class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
                
        s = 0
        stack = [(root, False)] 

        while stack:
            node, isLeftChild = stack.pop(0)
            
            if isLeftChild and not node.left and not node.right:
                s += node.val
            
            if node.right:
                stack.append((node.right, False))
            
            if node.left:
                stack.append((node.left, True))
        
        return s