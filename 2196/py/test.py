from typing import List, Optional, Self, Dict, Set, Deque
from collections import deque


class TreeNode:
    val: int
    left: Optional[Self]
    right: Optional[Self]
    def __init__(self, val: int = 0, left: Optional[Self] = None, right: Optional[Self] = None):
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
        


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        map: Dict[int, TreeNode] = dict()
        child: Set[int] = set()

        for pv, cv, is_left in descriptions:
            child.add(cv)

            p_node: TreeNode
            if pv in map:
                p_node = map[pv]
            else:
                p_node = TreeNode(pv)
                map[pv] = p_node

            if cv not in map:
                map[cv] = TreeNode(cv)

            if is_left:
                p_node.left = map[cv]
            else:
                p_node.right = map[cv]

        for pv, _, _ in descriptions:
            if pv not in child:
                return map[pv]


def main() -> None:
    descriptions: List[List[int]] = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
    res: Optional[TreeNode] = Solution().createBinaryTree(descriptions)
    print(res)


if __name__ == "__main__":
    main()
