# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        best = float("-infinity")

        def dfs(node):
            nonlocal best
            if not node: return 0

            l = dfs(node.left)
            r = dfs(node.right)

            passOn = max(l + node.val, r + node.val, node.val)
            best = max(best, l + r + node.val, passOn)
            return passOn

        dfs(root)
        return best

        