from typing import Self


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
        res: list[str] = []
        nodes: list[Self | None] = [self]
        while len(nodes) != 0:
            new_nodes: list[Self | None] = []
            for curr in nodes:
                if curr is None:
                    res.append("null")
                    continue
                res.append(str(curr.val))
                if curr.left:
                    new_nodes.append(curr.left)
                else:
                    new_nodes.append(None)
                if curr.right:
                    new_nodes.append(curr.right)
                else:
                    new_nodes.append(None)
            nodes = new_nodes
        while res[-1] == "null":
            res.pop(-1)
        return f"[ {', '.join(res)} ]"

    def __str__(self) -> str:
        return self.__repr__()

    @classmethod
    def from_list(cls, li: list[int | None]) -> Self:
        first: int | None = li.pop(0)
        if not first:
            return cls()
        root: Self = cls(first)
        nodes: list[Self] = [root]
        while li:
            left: int | None = li.pop(0)
            right: int | None = None
            if li:
                right = li.pop(0)
            parent: Self = nodes.pop(0)

            if left:
                node: Self = cls(left)
                parent.left = node
                nodes.append(node)
            if right:
                node: Self = cls(right)
                parent.right = node
                nodes.append(node)
        return root


class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        li: list[TreeNode] = []

        def dfs(root: TreeNode) -> None:
            nonlocal li
            li.append(root)
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)

        dfs(root)
        curr = root
        for node in li[1:]:
            curr.left = None
            curr.right = node
            curr = node
        curr.left = curr.right = None


root = [1, 2, 5, 3, 4, null, 6]
root = TreeNode.from_list(root)
Solution().flatten(root)
print(root)
