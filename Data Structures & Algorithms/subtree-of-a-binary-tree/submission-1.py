# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and subRoot:
            return False
            
        if vSubtree(root, subRoot):
            return True
        
        lSubtree = self.isSubtree(root.left, subRoot)
        rSubtree = self.isSubtree(root.right, subRoot)
        if lSubtree or rSubtree:
            return True
        else:
            return False


def vSubtree(root, sub):
    if not root and not sub:
        return True

    if root and sub and root.val == sub.val:
        return vSubtree(root.left, sub.left) and vSubtree(root.right, sub.right)
    else:
        return False


        