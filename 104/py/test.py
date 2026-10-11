# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        depth: int = 0
        if not root.left and not root.right:
            return 1
        if root.left:
            depth = self.maxDepth(root.left)
        if root.right:
            depth = max(depth, self.maxDepth(root.right))
        return depth + 1
