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
        curr: bool = False
        if root.val in delete_set:
            curr = True
        else:
            res.append(root)

        if root.left:
            self.bfs(root.left, delete_set, res, root, True, curr)
        if root.right:
            self.bfs(root.right, delete_set, res, root, False, curr)


        return res


    def bfs(self, root: TreeNode, to_delete: Set[int], res: List[TreeNode], parent: TreeNode, is_left: bool, parent_deleted: bool) -> None:
        curr: bool = False

        if root.val in to_delete:
            curr = True
            if is_left:
                parent.left = None
            else:
                parent.right = None
        else:
            if parent_deleted:
                res.append(root)

        if root.left:
            self.bfs(root.left, to_delete, res, root, True, curr)
        if root.right:
            self.bfs(root.right, to_delete, res, root, False, curr)


def main():
    lst: List[Optional[int]] = [1,2,3,4,5,6,7]
    root: TreeNode = TreeNode.from_list(lst)
    to_delete: List[int] = [3,5]
    
    res: List[TreeNode] = Solution().delNodes(root, to_delete)
    print(res)


if __name__ == "__main__":
    main()
