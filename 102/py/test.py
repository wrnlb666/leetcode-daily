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
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        res: list[list[int]] = []
        if not root:
            return res

        parents: list[TreeNode] = [root]
        res: list[list[int]] = []

        while parents:
            new_parents: list[TreeNode] = []
            curr: list[int] = []
            for parent in parents:
                curr.append(parent.val)
                if parent.left:
                    new_parents.append(parent.left)
                if parent.right:
                    new_parents.append(parent.right)
            res.append(curr)
            parents = new_parents

        return res


root = [3, 9, 20, null, null, 15, 7]
root = TreeNode.from_list(root)
print(Solution().levelOrder(root))
