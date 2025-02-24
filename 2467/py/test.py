from typing import List, Deque, Dict, Tuple
from collections import deque


class Solution:
    bob_path: Dict[int, int]
    visited: List[int]
    tree: List[List[int]]

    def __init__(self):
        self.bob_path = dict()
        self.visited = list()
        self.tree = list()

    def mostProfitablePath(
        self, edges: List[List[int]], bob: int, amount: List[int]
    ) -> int:
        n: int = len(amount)
        res: int = -(2**31) - 1
        self.tree = [[] for _ in range(n)]
        self.bob_path = {}
        self.visited = [False] * n
        node_queue: Deque[Tuple[int, int, int]] = deque([(0, 0, 0)])

        for edge in edges:
            self.tree[edge[0]].append(edge[1])
            self.tree[edge[1]].append(edge[0])

        self.find_bob_path(bob, 0)

        self.visited = [False] * n
        while node_queue:
            source_node, time, income = node_queue.popleft()

            if source_node not in self.bob_path or time < self.bob_path[source_node]:
                income += amount[source_node]
            elif time == self.bob_path[source_node]:
                income += amount[source_node] // 2

            if len(self.tree[source_node]) == 1 and source_node != 0:
                res = max(res, income)

            for adjacent_node in self.tree[source_node]:
                if not self.visited[adjacent_node]:
                    node_queue.append((adjacent_node, time + 1, income))

            self.visited[source_node] = True

        return res

    def find_bob_path(self, source_node, time):
        self.bob_path[source_node] = time
        self.visited[source_node] = True

        if source_node == 0:
            return True

        for adjacent_node in self.tree[source_node]:
            if not self.visited[adjacent_node]:
                if self.find_bob_path(adjacent_node, time + 1):
                    return True

        self.bob_path.pop(source_node, None)
        return False


def main() -> None:
    edges: List[List[int]] = [[0, 1], [1, 2], [1, 3], [3, 4]]
    bob: int = 3
    amount: List[int] = [-2, 4, 2, -4, 6]
    res: int = Solution().mostProfitablePath(edges, bob, amount)
    print(res)


if __name__ == "__main__":
    main()
