from typing import Optional, Self, List, Deque
from collections import deque
import math


null: None = None


class TreeNode:
    def __init__(
        self,
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
    def minimumDiameterAfterMerge(
        self, edges1: list[list[int]], edges2: list[list[int]]
    ) -> int:
        n = len(edges1) + 1
        m = len(edges2) + 1

        adj_list1 = self.build_adj_list(n, edges1)
        adj_list2 = self.build_adj_list(m, edges2)

        diameter1, _ = self.find_diameter(adj_list1, 0, -1)
        diameter2, _ = self.find_diameter(adj_list2, 0, -1)

        combined_diameter = math.ceil(diameter1 / 2) + math.ceil(diameter2 / 2) + 1

        return max(diameter1, diameter2, combined_diameter)

    def build_adj_list(self, size: int, edges: list[list[int]]) -> list[list[int]]:
        adj_list = [[] for _ in range(size)]
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])
        return adj_list

    def find_diameter(
        self, adj_list: list[list[int]], node: int, parent: int
    ) -> tuple[int, int]:
        max_depth1 = max_depth2 = 0
        diameter = 0

        for neighbor in adj_list[node]:
            if neighbor == parent:
                continue

            child_diameter, depth = self.find_diameter(adj_list, neighbor, node)
            depth += 1

            diameter = max(diameter, child_diameter)

            if depth > max_depth1:
                max_depth2 = max_depth1
                max_depth1 = depth
            elif depth > max_depth2:
                max_depth2 = depth

        diameter = max(diameter, max_depth1 + max_depth2)

        return diameter, max_depth1


def main() -> None:
    edges1: List[List[int]] = [[0, 1], [0, 2], [0, 3]]
    edges2: List[List[int]] = [[0, 1]]
    res: int = Solution().minimumDiameterAfterMerge(edges1, edges2)
    print(res)


if __name__ == "__main__":
    main()
