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
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        ancestor: Optional[TreeNode] = self.find_lca(root, startValue, destValue)
        path_start: List[int] = [0]
        path_dest: List[str] = [""]
        self.dfs_start(ancestor, path_start, startValue)
        self.dfs_dest(ancestor, path_dest, destValue)

        return 'U' * path_start[0] + path_dest[0]

    
    def dfs_start(self, root: Optional[TreeNode], path: List[int], target: int) -> bool:
        if root == None:
            return False

        if root.val == target:
            return True

        path[0] += 1
        
        if self.dfs_start(root.left, path, target) or self.dfs_start(root.right, path, target):
            return True

        path[0] -= 1
        return False

    
    def dfs_dest(self, root: Optional[TreeNode], path: List[str], target: int) -> bool:
        if root == None:
            return False

        if root.val == target:
            return True

        path[0] += 'L'
        if self.dfs_dest(root.left, path, target):
            return True
        path[0] = path[0][0:-1]

        path[0] += 'R'
        if self.dfs_dest(root.right, path, target):
            return True
        path[0] = path[0][0:-1]

        return False

    
    def find_lca(self, root: Optional[TreeNode], n1: int, n2: int) -> Optional[TreeNode]:
        p1: List[TreeNode] = []
        p2: List[TreeNode] = []

        if not self.find_path(root, p1, n1) or not self.find_path(root, p2, n2):
            return None

        i: int = 0
        while i < len(p1) and i < len(p2) and p1[i] == p2[i]:
            i += 1

        return p1[i - 1]


    def find_path(self, root: Optional[TreeNode], path: List[TreeNode], target: int) -> bool:
        if root == None:
            # reach end but finds nothing
            return False

        path.append(root)

        if root.val == target:
            # finds target
            return True

        if self.find_path(root.left, path, target) or self.find_path(root.right, path, target):
            return True

        path.pop()
        return False


def main() -> None:
    root: TreeNode = TreeNode.from_list([5, 1, 2, 3, None, 6, 4])
    startValue: int = 3
    destValue: int = 6

    res: str = Solution().getDirections(root, startValue, destValue)
    print(res)


if __name__ == "__main__":
    main()
