from typing import Optional, Self, List, Deque
from collections import deque
from heapq import heappush, heappop


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
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if root is None:
            return -1

        # sums: List[int] = list()
        sums: List[int] = list()
        
        # bfs to traverse all nodes level by level
        queue: Deque[TreeNode] = deque()
        queue.append(root)
        first: TreeNode = root
        new_level: bool = False
        sum: int = root.val
        while queue:
            node = queue.popleft()
            if node == first:
                # sums.append(sum)
                heappush(sums, sum)
                if len(sums) > k:
                    heappop(sums)
                sum = 0
                new_level = True
            if node.left is not None:
                queue.append(node.left)
                sum += node.left.val
                if new_level:
                    first = node.left
                    new_level = False
            if node.right is not None:
                queue.append(node.right)
                sum += node.right.val
                if new_level:
                    first = node.right
                    new_level = False

        if k > len(sums):
            return -1
        return sums[0]


def main() -> None:
    root: List[int | None] = [5,8,9,2,1,3,7,4,6]
    k: int = 2
    res: int = Solution().kthLargestLevelSum(TreeNode.from_list(root), k)
    print(res)


if __name__ == "__main__":
    main()
