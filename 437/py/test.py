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


from collections import Counter


class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        res: int = 0
        if not root:
            return res

        def dfs(root: TreeNode, curr: int, prefix: Counter[int]) -> None:
            nonlocal res, targetSum
            new_sum = curr + root.val
            if new_sum - targetSum in prefix:
                res += prefix[new_sum - targetSum]
            new_prefix = prefix.copy()
            new_prefix[new_sum] += 1
            if root.left:
                dfs(root.left, new_sum, new_prefix)
            if root.right:
                dfs(root.right, new_sum, new_prefix)

        prefix: Counter[int] = Counter()
        prefix[0] += 1
        dfs(root, 0, prefix)
        return res


root = [10, 5, -3, 3, 2, null, 11, 3, -2, null, 1]
targetSum = 8
root = TreeNode.from_list(root)
print(Solution().pathSum(root, targetSum))
