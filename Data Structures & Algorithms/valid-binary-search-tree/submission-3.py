# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, high, low):
            if not node: return True
            if node.val >= high or node.val <= low: return False
            if node.left and node.left.val >= node.val:
                return False
            if node.right and node.right.val <= node.val:
                return False
            
            return dfs(node.left, min(high, node.val), low) and dfs(node.right, high, max(low, node.val))
        
        return dfs(root, float("infinity"), float("-infinity"))
            
        