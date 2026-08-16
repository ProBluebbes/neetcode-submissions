# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hm = {}
        pre_idx = 0
        for i in range(len(inorder)):
            hm[inorder[i]] = i
        
        def dfs(l, r):
            nonlocal pre_idx
            if l > r: return None
            val = preorder[pre_idx]
            pre_idx += 1
            idx = hm[val]
            node = TreeNode(val)
            node.left = dfs(l, idx-1)
            node.right = dfs(idx+1, r)
            return node

        return dfs(0, len(inorder)-1)