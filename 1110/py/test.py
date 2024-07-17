from typing import Optional, Self, List, Deque, Set
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


class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        delete_set: Set[int] = set(to_delete)
        res: List[TreeNode] = []
        if root == None:
            return res

        if root.val not in delete_set:
            res.append(root)

        queue: Deque[TreeNode] = deque([root])
        while queue:
            node: TreeNode = queue.popleft()
            deleted: bool = False
            if node.val in delete_set:
                deleted = True
                    
            if node.left:
                queue.append(node.left)
                if node.left.val in delete_set:
                    node.left = None
                elif deleted:
                    res.append(node.left)
            if node.right:
                queue.append(node.right)
                if node.right.val in delete_set:
                    node.right = None
                elif deleted:
                    res.append(node.right)

        return res


def main():
    lst: List[Optional[int]] = [1,2,None,4,3]
    root: TreeNode = TreeNode.from_list(lst)
    to_delete: List[int] = [2,3]
    
    res: List[TreeNode] = Solution().delNodes(root, to_delete)
    print(res)


if __name__ == "__main__":
    main()
