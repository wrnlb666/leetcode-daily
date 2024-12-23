from typing import Optional, Self, List, Deque, Dict
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


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        def get_min(original: List[int]) -> int:
            swaps: int = 0
            target: List[int] = sorted(original)
            pos: Dict[int, int] = {val: idx for idx, val in enumerate(original)}

            for i in range(len(original)):
                if original[i] != target[i]:
                    swaps += 1
                    cur_pos = pos[target[i]]
                    pos[original[i]] = cur_pos
                    original[cur_pos] = original[i]

            return swaps
        
        queue: Deque[TreeNode] = deque([root])
        res: int = 0

        while queue:
            level_size: int = len(queue)
            level_values: List[int] = list()

            for _ in range(level_size):
                node: TreeNode = queue.popleft()
                level_values.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res += get_min(level_values)

        return res


def main() -> None:
    root: List[Optional[int]] = [1,4,3,7,6,8,5,null,null,null,null,9,null,10]
    res: int = Solution().minimumOperations(TreeNode.from_list(root))
    print(res)


if __name__ == "__main__":
    main()
