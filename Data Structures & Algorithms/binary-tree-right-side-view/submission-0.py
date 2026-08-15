# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        q.append((root, 1))
        res = []
        depth = 0

        while q:
            node, level = q.popleft()
            if not node:
                continue
            q.append((node.right, level + 1))
            q.append((node.left, level + 1))

            if depth < level:
                res.append(node.val)
                depth += 1

        return res

            