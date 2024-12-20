from typing import Optional, Self, List, Deque
from collections import deque


null: None = None
class TreeNode:
    def __init__(self,
                 val: int = 0,
                 left: Optional[Self] = None,
                 right: Optional[Self] = None,
                 ) -> None:
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        res: List[int | str] = []
        nodes: Deque[Optional[Self]] = deque()
        nodes.append(self)
        while len(nodes) != 0:
            curr: Optional[Self] = nodes.popleft()
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
    def from_list(cls, li: List[Optional[int]]) -> Self:
        first: Optional[int] = li.pop(0)
        if not first:
            return cls()
        root: Self = cls(first)
        queue: Deque[Self] = deque([root])
        while li:
            left: Optional[int] = li.pop(0)
            right: Optional[int] = None
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
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(
                left_child: Optional[TreeNode],
                right_child: Optional[TreeNode],
                level: int
        ) -> None:
            if left_child is None or right_child is None:
                return
            if level % 2 == 0:
                temp = left_child.val
                left_child.val = right_child.val
                right_child.val = temp

            dfs(left_child.left, right_child.right, level + 1)
            dfs(left_child.right, right_child.left, level + 1)

        if root is None:
            return root

        dfs(root.left, root.right, 0)
        return root



def main() -> None:
    root: List[Optional[int]] = [2,3,5,8,13,21,34]
    res: Optional[TreeNode] = Solution().reverseOddLevels(TreeNode.from_list(root))
    print(res)


if __name__ == "__main__":
    main()
