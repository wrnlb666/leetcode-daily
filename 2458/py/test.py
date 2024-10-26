from typing import Optional, Self, List, Deque, Dict, Tuple
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


class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        if root is None:
            return list()

        # dfs to traverse the entire tree
        heights: Dict[int, int] = dict()
        def dfs(root: Optional[TreeNode], height: int) -> int:
            if root is None:
                return height
            left: int = dfs(root.left, height+1)
            right: int = dfs(root.right, height+1)
            res: int = max(left, right)
            heights[root.val] = res
            return res
        dfs(root, -1)
        print(heights)

        # bfs to traverse the entire tree
        queue: Deque[TreeNode] = deque()
        queue.append(root)
        first: TreeNode = root
        new_level: bool = False
        level: int = -2
        cache: List[Tuple[int, int]] = [(-heights[root.val], root.val)]
        res: Dict[int, int] = dict()
        def fill_res(cache: List[Tuple[int, int]], res: Dict[int, int], lvl: int):
            cache.sort()
            if len(cache) > 1:
                res[cache[0][1]] = -cache[1][0]
                for n in cache[1:]:
                    res[n[1]] = -cache[0][0]
            else:
                print(cache)
                res[cache[0][1]] = lvl

        while queue:
            node = queue.popleft()
            if node == first:
                new_level = True
                fill_res(cache, res, level)
                level += 1
                cache.clear()
            if node.left is not None:
                queue.append(node.left)
                if new_level:
                    first = node.left
                    new_level = False
            if node.right is not None:
                queue.append(node.right)
                if new_level:
                    first = node.right
                    new_level = False
            cache.append((-heights[node.val], node.val))
        fill_res(cache, res, level)

        return [res[n] for n in queries]




def main() -> None:
    root: List[Optional[int]] = [8,6,37,3,7,33,65,1,4,null,null,29,36,51,66,null,2,null,5,26,31,35,null,45,58,null,null,null,null,null,null,22,28,30,32,34,null,44,47,55,59,21,25,27,null,null,null,null,null,null,null,41,null,46,48,54,56,null,62,13,null,24,null,null,null,38,42,null,null,null,49,53,null,null,57,60,64,11,20,23,null,null,39,null,43,null,50,52,null,null,null,null,61,63,null,10,12,18,null,null,null,null,40,null,null,null,null,null,null,null,null,null,null,9,null,null,null,16,19,null,null,null,null,15,17,null,null,14]
    queries: List[int] = [57,7,32,55,20,25,45,34,5,19,45,30,48,1,47,32,60,31,22,15,31]
    res: List[int] = Solution().treeQueries(TreeNode.from_list(root), queries)
    print(res)


if __name__ == "__main__":
    main()
