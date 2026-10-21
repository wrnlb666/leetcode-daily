from typing import Self
from collections import deque


null: None = None


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Self | None = None,
        right: Self | None = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        res: list[int | str] = []
        nodes: deque[Self | None] = deque()
        nodes.append(self)
        while len(nodes) != 0:
            curr: Self | None = nodes.popleft()
            if curr is None:
                res.append("null")
                continue
            res.append(curr.val)
            if curr.left is not None:
                nodes.append(curr.left)
                if curr.right is None:
                    nodes.append(None)
            if curr.right is not None:
                if curr.left is None:
                    nodes.append(None)
                nodes.append(curr.right)
        while res[-1] == "null":
            res.pop(-1)
        return str(res)

    def __str__(self) -> str:
        return self.__repr__()

    @classmethod
    def from_list(cls, li: list[int | None]) -> Self:
        first: int | None = li.pop(0)
        if not first:
            return cls()
        root: Self = cls(first)
        queue: deque[Self] = deque([root])
        while li:
            left: int | None = li.pop(0)
            right: int | None = None
            if li:
                right = li.pop(0)
            parent: Self = queue.popleft()

            if left:
                node: Self = cls(left)
                parent.left = node
                queue.append(node)
            if right:
                node: Self = cls(right)
                parent.right = node
                queue.append(node)
        return root


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        idx_map = {val: i for i, val in enumerate(inorder)}

        def build(pre_l: int, pre_r: int, in_l: int, in_r: int) -> TreeNode | None:
            if pre_l > pre_r:
                return None

            root_val = preorder[pre_l]
            root = TreeNode(root_val)
            mid = idx_map[root_val]
            left_size = mid - in_l
            root.left = build(pre_l + 1, pre_l + left_size, in_l, mid - 1)
            root.right = build(pre_l + left_size + 1, pre_r, mid + 1, in_r)
            return root

        return build(0, len(preorder) - 1, 0, len(inorder) - 1)


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
print(Solution().buildTree(preorder, inorder))
