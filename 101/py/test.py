# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        def dfs(left: TreeNode, right: TreeNode) -> bool:
            if not left and not right:
                return True
            if left.val != right.val:
                return False
            if bool(left.left) != bool(right.right) or bool(left.right) != bool(right.left):
                return False

            res: bool = True
            if left.left and right.right:
                res = dfs(left.left, right.right)
            if res and left.right and right.left:
                res = dfs(left.right, right.left)
            return res

        if not root:
            return True
        if not root.left and not root.right:
            return True
        if bool(root.left) != bool(root.right):
            return False

        return dfs(root.left, root.right)
