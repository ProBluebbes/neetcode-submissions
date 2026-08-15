# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # find p
        pPath = getNodePath(root, p.val)
        qPath = getNodePath(root, q.val)

        while True:
            if not pPath:
                break

            pNode = pPath.pop()

            for vNode in qPath:
                if vNode.val == pNode.val:
                    return pNode
        
        

def getNodePath(root, val):
    stack = []
    dfs(root, val, stack)
    return stack

def dfs(node, val, stack):
    if not node:
        return False

    stack.append(node)
    if node.val == val:
        return True

    if dfs(node.left, val, stack):
        return True
    if dfs(node.right, val, stack):
        return True

    stack.pop()    
    return False