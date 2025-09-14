from typing import Optional
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxDeph(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def dfs(root, depth):
            if not root:
                return depth
            
            left = dfs(root.left, depth+1)
            right = dfs(root.right, depth+1)
            
            return max(left, right)
                
        
        return dfs(root, 0)
        