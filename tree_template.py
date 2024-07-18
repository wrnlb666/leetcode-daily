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
            if curr == None:
                res.append("null")
                continue
            res.append(curr.val)
            if curr.left != None:
                nodes.append(curr.left)
                if curr.right == None:
                    nodes.append(None)
            if curr.right != None:
                if curr.left == None:
                    nodes.append(None)
                nodes.append(curr.right)
        while res[-1] == "null":
            res.pop(-1)
        return str(res)

    def __str__(self) -> str:
        return self.__repr__()

    @classmethod
    def from_list(cls, l: List[Optional[int]]) -> Self:
        first: Optional[int] = l.pop(0)
        if not first:
            return cls()
        root: Self = cls(first)
        queue: Deque[Self] = deque([root])
        while l:
            left: Optional[int] = l.pop(0)
            right: Optional[int] = None
            if l:
                right = l.pop(0)
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



