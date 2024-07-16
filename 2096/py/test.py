from typing import Optional, Self, List, Deque
from collections import deque


# Definition for a binary tree node.
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
                res.append("None")
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
        while res[-1] == "None":
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


class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        if root == None:
            return ""

        p1: List[str] = [""]
        p2: List[str] = [""]

        self.find_path(root, p1, startValue)
        self.find_path(root, p2, destValue)

        s1: str = p1[0]
        s2: str = p2[0]

        while s1 and s2 and s1[-1] == s2[-1]:
            s1 = s1[:-1]
            s2 = s2[:-1]

        return 'U' * (len(s1)) + s2[::-1]

    
    def find_path(self, root: TreeNode, path: List[str], target: int) -> bool:
        if root.val == target:
            return True

        if root.left and self.find_path(root.left, path, target):
            path[0] += 'L'
            return True

        if root.right and self.find_path(root.right, path, target):
            path[0] += 'R'
            return True

        return False


def main() -> None:
    lst: List[Optional[int]] = [5,1,2,3,None,6,4]
    root: TreeNode = TreeNode.from_list(lst)
    startValue: int = 3
    destValue: int = 6

    res: str = Solution().getDirections(root, startValue, destValue)
    print(res)


if __name__ == "__main__":
    main()
