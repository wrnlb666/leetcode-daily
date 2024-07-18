from typing import Optional, Deque, Self, Dict, List, Set
from collections import deque


null = None
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
    def countPairs(self, root: TreeNode, distance: int) -> int:
        # generate adjacency dict and leaves set
        adjacency: Dict[TreeNode, List[TreeNode]] = dict()
        leaves: Set[TreeNode] = set()

        # dfs to fill adjacency and leaves
        def dfs_conversion(node: TreeNode, parent: TreeNode) -> None:
            if node.left == None and node.right == None:
                leaves.add(node)
                adjacency[node] = [parent]
                return
            adjacency[node] = [parent]
            if node.left:
                adjacency[node].append(node.left)
                dfs_conversion(node.left, node)
            if node.right:
                dfs_conversion(node.right, node)
                adjacency[node].append(node.right)

        # perfrom dfs
        if root.left == None and root.right == None:
            leaves.add(root)
        else:
            adjacency[root] = []
            if root.left:
                adjacency[root].append(root.left)
                dfs_conversion(root.left, root)
            if root.right:
                dfs_conversion(root.right, root)
                adjacency[root].append(root.right)

        # find pairs
        res: int = 0

        # early return if `len(adjacency) == 0`
        if not adjacency:
            return res

        # dfs_wrapper
        def dfs(node: TreeNode) -> None:
            if node not in adjacency:
                return

            visited: Set[TreeNode] = set([node])

            # dfs
            def dfs_wrapped(node: TreeNode, distance: int) -> None:
                if distance == 0:
                    return

                visited.add(node)

                nonlocal res
                if node in leaves:
                    res += 1
                    return
                
                for n in adjacency[node]:
                    if n not in visited:
                        dfs_wrapped(n, distance - 1)

            dfs_wrapped(adjacency[node][0], distance)

        # perfrom dfs on all leaves
        for n in leaves:
            dfs(n)

        return res // 2


def main() -> None:
    lst: List[Optional[int]] = [1,2,3,null,4]
    root: TreeNode = TreeNode.from_list(lst)
    distance: int = 3

    res: int = Solution().countPairs(root, distance)
    print(res)


if __name__ == "__main__":
    main()
