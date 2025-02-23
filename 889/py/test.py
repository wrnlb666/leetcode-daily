from typing import Optional, Self, List, Deque
from collections import deque


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


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(
        self, preorder: List[int], postorder: List[int]
    ) -> Optional[TreeNode]:
        if not preorder:
            return None
        root: TreeNode = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root
        i: int = 0
        while preorder[1] != postorder[i]:
            i += 1
        i += 1
        # print(preorder[1 : i + 1], postorder[0:i])
        root.left = self.constructFromPrePost(preorder[1 : i + 1], postorder[0:i])
        # print(preorder[i + 1 :], postorder[i:-1])
        root.right = self.constructFromPrePost(preorder[i + 1 :], postorder[i:-1])
        return root


def main() -> None:
    preorder: List[int] = [2, 1]
    postorder: List[int] = [1, 2]
    res: Optional[TreeNode] = Solution().constructFromPrePost(preorder, postorder)
    print(res)


if __name__ == "__main__":
    main()
