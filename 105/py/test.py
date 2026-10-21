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
        if not preorder:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        root: int = preorder[0]
        im: int = inorder.index(root)
        in_left = inorder[:im]
        in_right = inorder[im + 1 :]
        pre_left = preorder[1 : im + 1]
        pre_right = preorder[im + 1 :]
        left = self.buildTree(pre_left, in_left)
        right = self.buildTree(pre_right, in_right)
        return TreeNode(root, left, right)


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
print(Solution().buildTree(preorder, inorder))
